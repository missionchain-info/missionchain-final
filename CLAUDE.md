# MissionChain Fullstack — Claude Code Project Guide

## Tổng Quan Hệ Thống

MissionChain là hệ sinh thái **Web3 đức tin** trên Binance Smart Chain (BSC), nhắm tới 2.6 tỷ tín hữu Kitô giáo. Sản phẩm cốt lõi: MIC token tiện ích, MICE mining license, MFP-NFT governance credentials, và SOPHIA AI assistant.

## Hai Thư Mục — Vai Trò Và Mối Quan Hệ

| Thư mục | Vai trò | Đặc điểm |
|---------|---------|-----------|
| **Mission Chain Fullstack** | Kho tài liệu **SOURCE OF TRUTH** | Chứa tất cả tài liệu nội bộ + public, là nơi chỉnh sửa đầu tiên |
| **Mission Chain (NEU)** | Repo **GitHub Pages** (`missionchain.io`) | Chỉ chứa file public, push lên GitHub để deploy trang web |

### Quy Trình Đồng Bộ

```
┌─────────────────────────────┐        ┌────────────────────────────────┐
│   Mission Chain Fullstack   │ ─sync→ │   Mission Chain (NEU)/         │
│   (Source of Truth)         │        │   missionchain/ (GitHub Pages) │
│                             │        │                                │
│  White Paper (html)/        │ ───→   │  frontend/documents/           │
│  DATA/                      │ ───→   │  (chỉ file public)             │
│  FOTO/                      │        │  (ảnh copy thủ công)           │
└─────────────────────────────┘        └────────────────────────────────┘
```

**Quan trọng:** Luôn chỉnh sửa ở Fullstack trước, sau đó sync sang NEU. Không chỉnh sửa trực tiếp trên NEU vì sẽ bị ghi đè.

---

## Bảng Đối Chiếu File Giữa Hai Thư Mục

### A. White Paper & Documents (Public — Sync 1:1)

| # | Fullstack (`White Paper (html)/`) | NEU (`frontend/documents/`) | Nội dung | Trạng thái |
|---|-----------------------------------|-----------------------------|----------|------------|
| 1 | `whitepaper.html` | `whitepaper.html` | White Paper chính — Tokenomics tổng quát, 3 pillars, governance | ✅ Synced |
| 2 | `documents-index.html` | `documents-index.html` | Trang hub dẫn đến tất cả tài liệu | ✅ Synced |
| 3 | `appendix-a.html` | `appendix-a.html` | **SEED Round**: 3.25% / 227.5M MIC @ $0.0025, vesting, packages | ✅ Synced |
| 4 | `appendix-b.html` | `appendix-b.html` | **Pre-Sale**: 4.50% / 315M MIC @ $0.005, referral F1:5%/F2:2% | ✅ Synced |
| 5 | `appendix-c.html` | `appendix-c.html` | **MICE License**: dynamic $300–$1,000, 360 days, max 100K | ✅ Synced |
| 6 | `appendix-d.html` | `appendix-d.html` | **Financial Projections**: revenue, MFP-NFT | ✅ Synced |
| 7 | `appendix-e.html` | `appendix-e.html` | **Adaptive Emission Engine**: E(t), pool split, circuit breakers | ✅ Synced |
| 8 | `appendix-f.html` | `appendix-f.html` | **Security & Audit**: Gnosis Safe, smart contract security | ✅ Synced |
| 9 | `appendix-g.html` | `appendix-g.html` | **AI Ops & Governance**: SOPHIA AI operations | ✅ Synced |
| 10 | `missionchain-dapp.html` | — (separate copy in `frontend/dapp/`) | **DApp UI**: full single-file DApp specification | ⚠ Xem mục B |

### B. DApp Files

| # | Fullstack (`White Paper (html)/`) | NEU (`frontend/dapp/`) | Nội dung | Ghi chú |
|---|-----------------------------------|-----------------------|----------|---------|
| 1 | `missionchain-dapp.html` | `missionchain-dapp.html` | DApp UI — staking, mining, portfolio, admin | NEU có phiên bản riêng, có thể khác |

### C. Landing Pages (Public — Sync 1:1)

| # | Fullstack (`DATA/`) | NEU (root) | Nội dung | Ghi chú |
|---|---------------------|------------|----------|---------|
| 1 | `mc_seed_round.html` | `mc_seed_round.html` | SEED Round landing page | ✅ Synced |
| 2 | `mc_announcement.html` | `mc_announcement.html` | Smart Contract Migration announcement | ✅ Synced |
| 3 | — (không có) | `index.html` | **Trang chủ missionchain.io** — landing page chính | ⚠ Chỉ tồn tại trên NEU |

### D. Files Chỉ Có Trên NEU (Public Website)

| # | NEU Path | Nội dung | Ghi chú |
|---|----------|----------|---------|
| 1 | `index.html` (~2,200 dòng) | Trang chủ missionchain.io — tokenomics overview, 3 pillars, MICE, sale rounds | **File quan trọng nhất cho public** |
| 2 | `White_Paper.html` (~1,800 dòng) | White Paper phiên bản website (khác với `whitepaper.html` trong documents/) | Phiên bản đầy đủ với formulas, governance |
| 3 | `Glossary_Brand_Terms.html` (~350 dòng) | Bảng thuật ngữ + công thức chính thức | Hướng dẫn dịch thuật, formula reference |
| 4 | `CLAUDE.md` | Hướng dẫn dự án cho Claude Code | Source of truth tokenomics |
| 5 | `CNAME` | Domain mapping: `missionchain.io` | Không chỉnh sửa |
| 6 | `scripts/deepl_translate_site.py` | Script dịch tự động qua DeepL API | Pipeline dịch thuật |
| 7 | `scripts/postprocess_public_translations.py` | Hậu xử lý bản dịch — sửa formula, link, label | Chứa formula templates cho 4 ngôn ngữ |
| 8 | `admin-content/private-website/` | Admin financial section (internal) | Không deploy public |

### E. Files Chỉ Có Trên Fullstack (Internal — Không Deploy)

| # | Fullstack Path | Nội dung | Mục đích |
|---|----------------|----------|----------|
| 1 | `DATA/adaptive-emission-engine-v1.html` | Thiết kế chi tiết Adaptive Emission Engine | Tài liệu nội bộ dev |
| 2 | `DATA/decision-log-v1.html` | Nhật ký quyết định (EM-01 ~ EM-06) | Lưu lý do thay đổi kiến trúc |
| 3 | `DATA/kickoff-review-report.html` | Báo cáo đánh giá kickoff | Phân tích rủi ro, timeline |
| 4 | `DATA/dev-team-process.html` | Quy trình dev team | Sprint, roles, workflows |
| 5 | `DATA/missionchain_fullstack-architecture-spec.html` | Kiến trúc fullstack v1.0 | Backend/frontend/DB specs |
| 6 | `DATA/missionchain-fullstack-architecture (neu).html` | Kiến trúc fullstack v2.0 (mới hơn) | Design system, component specs |
| 7 | `DATA/missionchain-web3-dapp-users (neu).html` | DApp User Interface spec (mới) | Wallet, staking, portfolio UX |
| 8 | `DATA/missionchain_web3-dapp_users.html` | DApp User Interface spec (cũ) | Phiên bản trước |
| 9 | `DATA/missionchain-web3-dapp-admin (neu).html` | Admin Console spec (mới) | Admin dashboard, controls |
| 10 | `DATA/missionchain_web3-dapp_admin.html` | Admin Console spec (cũ) | Phiên bản trước |
| 11 | `DATA/missionchain-sophia-brand-bible (neu).html` | SOPHIA AI brand bible | Brand identity, KOL strategy |
| 12 | `DATA/sophia-kol-vision.html` | SOPHIA KOL roadmap | AI KOL build plan |
| 13 | `DATA/social-media-strategy.html` | Chiến lược social media | Marketing channels, KPIs |
| 14 | `DATA/missionchain_world_frontend.html` | "Mission Chain World" frontend spec | UI components, navigation |
| 15 | `DATA/missionchain_world&io_admin.html` | World/IO admin interface | Admin controls |
| 16 | `FOTO/` (7 files) | Artwork SOPHIA & Claudia AI characters | Branding assets |

### F. Translations (NEU only — 4 ngôn ngữ × 5 files)

| Ngôn ngữ | Thư mục | Files |
|-----------|---------|-------|
| Español (ES) | `translations/es/` | index.html, White_Paper.html, Glossary_Brand_Terms.html, mc_seed_round.html, mc_announcement.html |
| Tiếng Việt (VI) | `translations/vi/` | (cùng 5 files) |
| 한국어 (KO) | `translations/ko/` | (cùng 5 files) |
| Português (PT) | `translations/pt/` | (cùng 5 files) |

**Pipeline dịch**: `deepl_translate_site.py` → `postprocess_public_translations.py` → commit → push

---

## Source of Truth — Tokenomics Chính Thức

### MIC Token (BEP-20 on BSC)

| Thông số | Giá trị |
|----------|---------|
| Total Supply | 7,000,000,000 MIC (hard cap) |
| Pre-Issued | 15% = 1,050,000,000 MIC |
| Mining Pool | 85% = 5,950,000,000 MIC |

### Pre-Issued 15% (6 categories)

| Category | % | MIC | Price | Vesting |
|----------|---|-----|-------|---------|
| Incentives & Airdrops | 0.25% | 17,500,000 | — | 10% unlock after 6 months, 2.5%/month |
| Seed Round | 3.25% | 227,500,000 | $0.0025 | 10% unlock after 6 months, 2.5%/month |
| Pre-Sale | 4.50% | 315,000,000 | $0.005 | 10% unlock after 6 months, 2.5%/month |
| DEX/CEX Listing | 1.50% | 105,000,000 | ~$0.01 | At listing |
| Founders & Mgmt | 4.00% | 280,000,000 | — | 10% unlock after 24 months, 2.5%/month |
| Treasure DAO | 1.50% | 105,000,000 | — | 10% unlock after 24 months, 0.25%/month |

### Mining Emission Split (85%)

| Pool | % | MIC |
|------|---|-----|
| Miners (MICE) | 60% | 3,570,000,000 |
| NFT Staking (Merged) | 20% | 1,190,000,000 |
| DAO Treasure | 15% | 892,500,000 |
| Buyback & Burn | 5% | 297,500,000 |

### Adaptive Emission Engine

```
E(t) = E_base(t) × D(t) × R(t)

E_base(t) = E₀ × e^(−λt)           // Exponential decay
E₀ ≈ 22,907,500 MIC/day             // Initial emission rate
T_half = 180 days                    // ~3 years to 99% emitted

D(t) = 0.5 + U(t)                   // Demand factor [0.5, 1.5]
R(t) = clamp(250%/ROI, 0.5, 2.0)    // ROI regulator
```

### MICE License

| Thông số | Giá trị |
|----------|---------|
| Type | ERC-1155 NFT |
| Duration | 360 days |
| Max Supply | 100,000 (slot recycling) |
| Pricing | Dynamic $300 – $1,000 USDT |
| Revenue Split | 50% Treasury / 30% Liquidity / 20% Buyback & Burn |

### NFT Staking (Merged Pool — 20%)

| Tier | Multiplier | Staking Cap |
|------|-----------|-------------|
| MFP-NFT | ×10 | 1,000,000 MIC |
| Platinum | ×5 | 500,000 MIC |
| Gold | ×2.5 | 250,000 MIC |
| Silver | ×1 | 100,000 MIC |
| No-NFT | ×0.5 | 50,000 MIC |

Time-lock: 30d=1× / 90d=1.25× / 180d=1.5× / 360d=2×

### Referral Program

- **Pre-Sale ONLY** (NOT Seed Round)
- F1: 5% USDT / F2: 2% USDT
- Payment: USDT + BNB only

### Circuit Breakers

1. Cumulative cap: totalEmitted ≤ 5,950,000,000
2. Daily cap: 2× E_base(t)
3. Price floor: $0.001 MIC
4. Unstake limit: 10%/day
5. Emergency pause: Gnosis Safe 3-of-5 multisig

### SEED Packages (@ $0.0025/MIC + 15% bonus)

| Package | Price | Base MIC | With Bonus |
|---------|-------|----------|------------|
| Basic | $500 | 200,000 | 230,000 |
| Standard | $1,000 | 400,000 | 460,000 |
| Pro | $2,000 | 800,000 | 920,000 |
| Elite | $5,000 | 2,000,000 | 2,300,000 |
| Pro Advanced | $10,000 | 4,000,000 | 4,600,000 |

### Pre-Sale Packages (@ $0.005/MIC + 10% bonus)

| Package | Price | Base MIC | With Bonus |
|---------|-------|----------|------------|
| Standard | $100 | 20,000 | 22,000 |
| Pro | $500 | 100,000 | 110,000 |
| Elite | $1,000 | 200,000 | 220,000 |
| Diamond | $5,000 | 1,000,000 | 1,100,000 |

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Blockchain | BSC (BNB Smart Chain) |
| Contracts | Solidity, Hardhat, OpenZeppelin |
| Oracle | PancakeSwap V3 TWAP (primary), Chainlink (fallback) |
| Admin | Gnosis Safe 3-of-5 multisig |
| KYC | Sumsub (off-chain) + on-chain allowlist |
| Frontend | Single-file HTML, CSS variables, dark/light mode |
| Design System | Cinzel + Rajdhani + Space Mono, gold #C9A84C, purple #5B2D9E |
| AI | SOPHIA — AI mentor/KOL, powered by LLM |
| Translations | DeepL API + custom postprocessing |

---

## Quy Tắc Khi Chỉnh Sửa

### ⚠ KHÔNG BAO GIỜ

- Commit `.env` hoặc file chứa secrets/API keys
- Chỉnh sửa trực tiếp trên NEU mà không sync từ Fullstack
- Thay đổi tokenomics numbers mà không cập nhật TẤT CẢ files liên quan
- Sử dụng dữ liệu cũ: `2,037,671` / `E_base × B × D(t) × L(t)` / `65%/15%/10%/10%` / `B = 6.5`

### ✅ LUÔN LUÔN

- Chỉnh sửa Fullstack trước, NEU sau
- Cập nhật cả 4 bản dịch khi thay đổi file EN
- Chạy `postprocess_public_translations.py` sau khi dịch mới
- Verify bằng grep toàn bộ repo trước khi push
- Đối chiếu với bảng tokenomics ở trên khi có nghi ngờ

### Git Workflow (NEU repo)

```bash
# 1. Copy files đã sửa từ Fullstack sang NEU
# 2. Stage changes
git add [files...]
# 3. Commit
git commit -m "Description of changes"
# 4. Push (cần PAT token)
git remote set-url origin https://TOKEN@github.com/missionchain-info/missionchain.git
git push origin main
git remote set-url origin https://github.com/missionchain-info/missionchain.git  # remove token
```

Account: `missionchain-info` — Email: `missionchain.info@gmail.com`

---

## Phân Loại Nội Dung Theo Chủ Đề

### Tokenomics & Kinh Tế

| File | Folder | Nội dung chính |
|------|--------|---------------|
| appendix-a.html | Both | SEED Round structure |
| appendix-b.html | Both | Pre-Sale structure |
| appendix-c.html | Both | MICE License |
| appendix-e.html | Both | Adaptive Emission Engine |
| adaptive-emission-engine-v1.html | Fullstack only | Chi tiết engine design |
| decision-log-v1.html | Fullstack only | Quyết định kinh tế (EM-01~EM-06) |

### Kiến Trúc & Kỹ Thuật

| File | Folder | Nội dung chính |
|------|--------|---------------|
| missionchain_fullstack-architecture-spec.html | Fullstack only | Architecture v1.0 |
| missionchain-fullstack-architecture (neu).html | Fullstack only | Architecture v2.0 |
| appendix-f.html | Both | Security & Audit |
| appendix-g.html | Both | AI Operations |

### DApp Interface

| File | Folder | Nội dung chính |
|------|--------|---------------|
| missionchain-dapp.html | Both | DApp UI chính |
| missionchain-web3-dapp-users (neu).html | Fullstack only | User DApp spec (mới) |
| missionchain_web3-dapp_users.html | Fullstack only | User DApp spec (cũ) |
| missionchain-web3-dapp-admin (neu).html | Fullstack only | Admin Console (mới) |
| missionchain_web3-dapp_admin.html | Fullstack only | Admin Console (cũ) |

### Branding & Marketing

| File | Folder | Nội dung chính |
|------|--------|---------------|
| missionchain-sophia-brand-bible (neu).html | Fullstack only | SOPHIA brand identity |
| sophia-kol-vision.html | Fullstack only | SOPHIA KOL roadmap |
| social-media-strategy.html | Fullstack only | Social media plan |
| FOTO/ (7 images) | Fullstack only | SOPHIA & Claudia artwork |

### Website & Public Content

| File | Folder | Nội dung chính |
|------|--------|---------------|
| index.html | NEU only | Trang chủ missionchain.io |
| White_Paper.html | NEU only | White Paper website version |
| Glossary_Brand_Terms.html | NEU only | Glossary + formula reference |
| mc_seed_round.html | Both | SEED Round landing page |
| mc_announcement.html | Both | Announcement page |
