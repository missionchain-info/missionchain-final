#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import requests
from bs4 import BeautifulSoup
from bs4.element import Comment, NavigableString, Tag
from requests.exceptions import RequestException


ROOT = Path("/Users/ledangtuan/Documents/Mission Chain")
SOURCE_FILES = [
    "index.html",
    "White_Paper.html",
    "Glossary_Brand_Terms.html",
    "mc_announcement.html",
    "mc_seed_round.html",
]
TARGETS = {
    "es": "ES",
    "pt": "PT-BR",
    "ko": "KO",
    "vi": "VI",
}
ASSET_EXTENSIONS = (".png", ".jpg", ".jpeg", ".svg", ".webp", ".gif", ".ico")
SKIP_TAGS = {"script", "style", "noscript"}
SKIP_ATTRS = {"href", "src", "srcset"}
TRANSLATABLE_ATTRS = ("placeholder", "title", "aria-label", "value", "alt")
FORMULA_PATTERNS = [
    re.compile(r"\b[A-Za-z][A-Za-z0-9_]*\([^)]*\)"),
    re.compile(r"\b[A-Za-z]+_[A-Za-z0-9_]+\b"),
    re.compile(r"\b[A-Z]{2,}(?:-[A-Z0-9]+)*\b"),
    re.compile(r"0\.\d+\^\([^)]+\)"),
    re.compile(r"Clamp\[[^\]]+\]"),
]


@dataclass
class PendingText:
    key: str
    text: str
    leading_ws: str
    trailing_ws: str
    placeholder_map: dict[str, str]


class DeepLClient:
    def __init__(self, api_key: str) -> None:
        self.session = requests.Session()
        self.session.headers.update(
            {
                "Authorization": f"DeepL-Auth-Key {api_key}",
                "Content-Type": "application/json",
            }
        )
        self.base_url = "https://api.deepl.com"

    def translate_batch(self, texts: list[str], target_lang: str) -> list[str]:
        payload = {
            "text": texts,
            "target_lang": target_lang,
            "source_lang": "EN",
            "preserve_formatting": True,
        }
        delay = 1.5
        last_error: Exception | None = None
        for _ in range(6):
            try:
                response = self.session.post(
                    f"{self.base_url}/v2/translate",
                    data=json.dumps(payload),
                    timeout=120,
                )
                response.raise_for_status()
                data = response.json()
                return [item["text"] for item in data["translations"]]
            except RequestException as exc:
                last_error = exc
                time.sleep(delay)
                delay = min(delay * 2, 20)
        raise RuntimeError(f"DeepL translation failed after retries: {last_error}")


def read_glossary_terms(glossary_path: Path) -> list[str]:
    soup = BeautifulSoup(glossary_path.read_text(), "html.parser")
    terms: set[str] = set()

    for cell in soup.select("table.glossary-table tbody tr td:first-child"):
        raw = " ".join(cell.stripped_strings).strip()
        if not raw:
            continue
        terms.add(raw)
        for part in re.split(r"\s*/\s*", raw):
            part = part.strip()
            if part:
                terms.add(part)

    manual_terms = {
        "Mission Chain",
        "Mission Chain Network",
        "Mission DAO",
        "Mission Network",
        "Mission Network Layer 2",
        "Creator Mission Economy",
        "Mission Learn",
        "Mission Work",
        "Mission Social",
        "Mission Arts",
        "Mission Hub",
        "Mission Social Festival",
        "MIC",
        "Mission Chain Token",
        "MICE",
        "Mission Algorithm Node License",
        "MFP-NFT",
        "Mission Founding Partner NFT",
        "Community NFT",
        "Builder NFT",
        "Maker NFT",
        "Luminary NFT",
        "NIRA-AI",
        "USDT",
        "BSC",
        "BEP-20",
        "DAO",
        "NFT",
        "Hindex",
        "White Paper",
        "Glossary of Brand Terms",
        "Smart Contract",
    }
    terms.update(manual_terms)
    return sorted(terms, key=len, reverse=True)


def is_meaningful_text(text: str) -> bool:
    stripped = text.strip()
    if not stripped:
        return False
    if not re.search(r"[A-Za-z]", stripped):
        return False
    if re.fullmatch(r"[\W_]+", stripped):
        return False
    return True


def protect_formulas(text: str, placeholders: dict[str, str], counter_start: int) -> tuple[str, int]:
    counter = counter_start
    protected = text
    for pattern in FORMULA_PATTERNS:
        matches = sorted(set(pattern.findall(protected)), key=len, reverse=True)
        for match in matches:
            token = f"MCPLH{counter:05d}"
            counter += 1
            placeholders[token] = match
            protected = protected.replace(match, token)
    return protected, counter


def protect_terms(text: str, terms: list[str]) -> tuple[str, dict[str, str]]:
    protected = text
    placeholders: dict[str, str] = {}
    counter = 0
    for term in terms:
        if term not in protected:
            continue
        token = f"MCPLH{counter:05d}"
        counter += 1
        placeholders[token] = term
        protected = protected.replace(term, token)
    protected, _ = protect_formulas(protected, placeholders, counter)
    return protected, placeholders


def restore_placeholders(text: str, placeholders: dict[str, str]) -> str:
    restored = text
    for token, original in sorted(placeholders.items(), key=lambda item: len(item[0]), reverse=True):
        restored = restored.replace(token, original)
    return restored


def collect_pending_texts(soup: BeautifulSoup, terms: list[str]) -> tuple[dict[str, PendingText], dict[str, object]]:
    pending: dict[str, PendingText] = {}
    references: dict[str, object] = {}
    counter = 0

    for node in soup.find_all(string=True):
        if isinstance(node, Comment):
            continue
        parent = node.parent
        if not isinstance(parent, Tag):
            continue
        if parent.name in SKIP_TAGS:
            continue
        if parent.has_attr("data-no-translate"):
            continue
        raw = str(node)
        if not is_meaningful_text(raw):
            continue
        leading = raw[: len(raw) - len(raw.lstrip())]
        trailing = raw[len(raw.rstrip()) :]
        core = raw.strip()
        protected, placeholders = protect_terms(core, terms)
        if protected == core and not placeholders:
            protected = core
        key = f"text-{counter}"
        counter += 1
        pending[key] = PendingText(
            key=key,
            text=protected,
            leading_ws=leading,
            trailing_ws=trailing,
            placeholder_map=placeholders,
        )
        references[key] = node

    for tag in soup.find_all(True):
        for attr in TRANSLATABLE_ATTRS:
            value = tag.get(attr)
            if not value or attr in SKIP_ATTRS:
                continue
            if not is_meaningful_text(value):
                continue
            leading = value[: len(value) - len(value.lstrip())]
            trailing = value[len(value.rstrip()) :]
            core = value.strip()
            protected, placeholders = protect_terms(core, terms)
            key = f"attr-{counter}"
            counter += 1
            pending[key] = PendingText(
                key=key,
                text=protected,
                leading_ws=leading,
                trailing_ws=trailing,
                placeholder_map=placeholders,
            )
            references[key] = (tag, attr)

    return pending, references


def chunk_pending(pending: Iterable[PendingText], max_items: int = 40, max_chars: int = 18000) -> Iterable[list[PendingText]]:
    batch: list[PendingText] = []
    chars = 0
    for item in pending:
        item_len = len(item.text)
        if batch and (len(batch) >= max_items or chars + item_len > max_chars):
            yield batch
            batch = []
            chars = 0
        batch.append(item)
        chars += item_len
    if batch:
        yield batch


def rewrite_local_paths(soup: BeautifulSoup) -> None:
    for tag in soup.find_all(True):
        for attr in ("href", "src"):
            value = tag.get(attr)
            if not value:
                continue
            if value.startswith(("#", "http://", "https://", "mailto:", "tel:", "data:", "javascript:")):
                continue
            if value in SOURCE_FILES:
                continue
            lowered = value.lower()
            if lowered.endswith(ASSET_EXTENSIONS):
                if not value.startswith("../"):
                    tag[attr] = f"../../{value}"


def translate_html(source_path: Path, output_path: Path, client: DeepLClient, target_lang: str, terms: list[str]) -> None:
    soup = BeautifulSoup(source_path.read_text(), "html.parser")
    if soup.html is not None:
        soup.html["lang"] = target_lang.lower()

    pending, references = collect_pending_texts(soup, terms)
    items = list(pending.values())
    total = len(items)
    if total == 0:
        rewrite_local_paths(soup)
        output_path.write_text(str(soup))
        return

    for batch_index, batch in enumerate(chunk_pending(items), start=1):
        translated = client.translate_batch([item.text for item in batch], target_lang)
        for item, translated_text in zip(batch, translated):
            translated_text = restore_placeholders(translated_text, item.placeholder_map)
            final_text = f"{item.leading_ws}{translated_text}{item.trailing_ws}"
            ref = references[item.key]
            if isinstance(ref, NavigableString):
                ref.replace_with(final_text)
            else:
                tag, attr = ref
                tag[attr] = final_text
        print(
            f"[{target_lang}] {source_path.name}: batch {batch_index} complete ({min(batch_index * 40, total)}/{total})",
            file=sys.stderr,
        )
        time.sleep(0.15)

    rewrite_local_paths(soup)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(str(soup))


def main() -> int:
    parser = argparse.ArgumentParser(description="Translate Mission Chain HTML files using DeepL while preserving glossary terms.")
    parser.add_argument("--langs", nargs="+", default=["es", "pt", "ko", "vi"], help="Language folders to generate")
    args = parser.parse_args()

    api_key = os.environ.get("DEEPL_API_KEY")
    if not api_key:
        print("DEEPL_API_KEY is required", file=sys.stderr)
        return 1

    terms = read_glossary_terms(ROOT / "Glossary_Brand_Terms.html")
    client = DeepLClient(api_key)

    translations_root = ROOT / "translations"
    translations_root.mkdir(exist_ok=True)

    for lang_key in args.langs:
        if lang_key not in TARGETS:
            raise SystemExit(f"Unsupported language key: {lang_key}")
        target_lang = TARGETS[lang_key]
        out_dir = translations_root / lang_key
        out_dir.mkdir(parents=True, exist_ok=True)
        for filename in SOURCE_FILES:
            translate_html(ROOT / filename, out_dir / filename, client, target_lang, terms)

    readme = translations_root / "README.md"
    readme.write_text(
        "\n".join(
            [
                "# Translations",
                "",
                "Generated with `scripts/deepl_translate_site.py`.",
                "",
                "Languages:",
                "- `es` -> Spanish",
                "- `pt` -> Portuguese (Brazil)",
                "- `ko` -> Korean",
                "- `vi` -> Vietnamese",
                "",
                "Files generated per language:",
                *[f"- `{name}`" for name in SOURCE_FILES],
            ]
        )
        + "\n"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
