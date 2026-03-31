from pathlib import Path
import re

ROOT = Path("/Users/ledangtuan/Documents/Mission Chain")
LOCALES = ["en", "es", "pt", "ko", "vi"]
PAGES = ["index.html", "White_Paper.html", "Glossary_Brand_Terms.html", "mc_seed_round.html", "mc_announcement.html"]

LANG_LABELS = {
    "en": "🇬🇧 EN",
    "es": "🇪🇸 ES",
    "pt": "🇧🇷 PT",
    "ko": "🇰🇷 KO",
    "vi": "🇻🇳 VI",
}

GLOSSARY_TOP = {
    "en": ("Website", "White Paper", "Glossary"),
    "es": ("Sitio web de Mission Chain", "White Paper", "Glosario"),
    "pt": ("Site da Mission Chain", "White Paper", "Glossario"),
    "ko": ("Mission Chain 웹사이트", "White Paper", "용어집"),
    "vi": ("Website Mission Chain", "White Paper", "Thuật ngữ"),
}

GLOSSARY_DOC_LINKS = {
    "es": ("Sitio web de Mission Chain", "White Paper"),
    "pt": ("Site da Mission Chain", "White Paper"),
    "ko": ("Mission Chain 웹사이트", "White Paper"),
    "vi": ("Website Mission Chain", "White Paper"),
}

WHITEPAPER_DOC_LINKS = {
    "es": ("Sitio web de Mission Chain", "Glosario de Terminos de Marca"),
    "pt": ("Site da Mission Chain", "Glossario de Termos da Marca"),
    "ko": ("Mission Chain 웹사이트", "브랜드 용어집"),
    "vi": ("Website Mission Chain", "Bang Thuat ngu Thuong hieu"),
}

WHITEPAPER_APPENDIX = {
    "es": {
        "A": "A. Seed Round",
        "B": "B. Pre-Sale",
        "C": "C. Estructura de Venta de MICE",
        "D": "D. Especificacion Economica Formal",
        "E": "E. Estrategia de Entrada al Mercado",
        "F": "F. Legal, Descargos y Privacidad",
        "G": "G. Proyecciones Financieras (Interno)",
        "H": "H. Operaciones DAO (Interno)",
        "I": "I. Operaciones NIRA-AI (Interno)",
    },
    "pt": {
        "A": "A. Seed Round",
        "B": "B. Pre-Sale",
        "C": "C. Estrutura de Venda de MICE",
        "D": "D. Especificacao Economica Formal",
        "E": "E. Estrategia de Entrada no Mercado",
        "F": "F. Legal, Avisos e Privacidade",
        "G": "G. Projecoes Financeiras (Interno)",
        "H": "H. Operacoes DAO (Interno)",
        "I": "I. Operacoes NIRA-AI (Interno)",
    },
    "ko": {
        "A": "A. Seed Round",
        "B": "B. Pre-Sale",
        "C": "C. MICE 판매 구조",
        "D": "D. 경제 공식 명세",
        "E": "E. 시장 진입 전략",
        "F": "F. 법률, 고지 및 개인정보",
        "G": "G. 재무 전망 (내부)",
        "H": "H. DAO 운영 (내부)",
        "I": "I. NIRA-AI 운영 (내부)",
    },
    "vi": {
        "A": "A. Seed Round",
        "B": "B. Pre-Sale",
        "C": "C. Cau truc Ban MICE",
        "D": "D. Dac ta Kinh te Chinh thuc",
        "E": "E. Chien luoc Tham nhap Thi truong",
        "F": "F. Phap ly, Tuyen bo va Quyen rieng tu",
        "G": "G. Du bao Tai chinh (Noi bo)",
        "H": "H. Van hanh DAO (Noi bo)",
        "I": "I. Ho tro Van hanh NIRA-AI (Noi bo)",
    },
}

ROUTE_HELPER = r"""
const SUPPORTED_LOCALES = ['en','es','pt','ko','vi'];
const LOCALE_LABELS = { en: '🇬🇧 EN', es: '🇪🇸 ES', pt: '🇧🇷 PT', ko: '🇰🇷 KO', vi: '🇻🇳 VI' };
function detectLocale() {
  const match = window.location.pathname.match(/\/translations\/(es|pt|ko|vi)(?:\/|$)/);
  return match ? match[1] : 'en';
}
function detectFileName(fallback) {
  const path = window.location.pathname || '';
  const cleanPath = path.endsWith('/') ? path.slice(0, -1) : path;
  const name = cleanPath.split('/').pop();
  return name || fallback;
}
function getLocalizedHref(lang, fallbackFile) {
  const currentLocale = detectLocale();
  const file = detectFileName(fallbackFile);
  const suffix = window.location.search + window.location.hash;
  if (currentLocale === 'en') {
    return (lang === 'en' ? file : 'translations/' + lang + '/' + file) + suffix;
  }
  return (lang === 'en' ? '../../' + file : '../' + lang + '/' + file) + suffix;
}
""".strip()

GLOSSARY_FORMULA_BLOCKS = {
    "es": """
<section class="section anim a1" id="math">
<div class="section-num">Seccion 7</div>
<h2 class="section-title">Variables de Formulas Matematicas</h2>
<p>Todas las formulas matematicas, nombres de variables, notacion funcional y constantes numericas en los documentos de Mission Chain deben conservarse exactamente como estan escritas en ingles, sin localizar simbolos, separadores ni notacion.</p>
<p>Mission Chain utiliza el punto (.) como separador decimal internacional en todas las formulas, por ejemplo 0.60, 0.95 y 22,907,500. No sustituya estos valores por comas ni por convenciones numericas locales dentro de la notacion de formula.</p>
<div class="wp-table-wrap"><table class="wp-table formula-table"><thead><tr><th>Formula / Variable</th><th>Definicion / Significado de cada variable</th></tr></thead><tbody>
<tr><td><span class="formula-math">E(t) = E<sub>base</sub> × B × D(t) × L(t)</span></td><td>Formula diaria de emision MIC. t es el numero de dias transcurridos desde la genesis del ecosistema. Los cuatro componentes se multiplican para producir E(t), la emision total de MIC liberada a la red en el dia t.</td></tr>
<tr><td><span class="formula-math">E₀ ≈ 22,907,500 MIC/day</span></td><td>Tasa inicial de emision diaria bajo el Adaptive Emission Engine. Combinada con decay exponencial (T_half = 180 dias), distribuye exactamente 5,950,000,000 MIC (85% del suministro total) al pool de mineria.</td></tr>
<tr><td><span class="formula-math">D(t) = 0.5 + U(t)</span></td><td>Factor de demanda. U(t) = tasa de utilizacion de MICE. Rango [0.5, 1.5]. Ajusta la emision en base a la demanda.</td></tr>
<tr><td><span class="formula-math">R(t) = clamp(250%/ROI, 0.5, 2.0)</span></td><td>Regulador de ROI. ROI objetivo = 250%. Limitado entre 0.5 y 2.0.</td></tr>
<tr><td><span class="formula-math">R<sub>MICE,i</sub>(t) = (M<sub>i</sub> / N<sub>t</sub>) × 0.60 × E(t)</span></td><td>Recompensa diaria MIC del operador MICE i en el dia t. M<sub>i</sub> es el numero de licencias MICE activas del operador i. N<sub>t</sub> es el total de licencias MICE activas en la red. 0.60 representa el 60% de la emision diaria asignada al pool Miners.</td></tr>
<tr><td><span class="formula-math">VotingWeight<sub>MFP,i</sub> = S<sub>i</sub> / Σ S<sub>MFP,active</sub></span></td><td>Peso de voto del holder i de MFP-NFT. S<sub>i</sub> es el MIC staked por el holder i. Σ S<sub>MFP,active</sub> es la suma del MIC staked por todos los holders MFP activos.</td></tr>
<tr><td><span class="formula-math">PoolShare<sub>NFT,i</sub>(t) = (S<sub>i</sub> × tier_mult / Σ weighted_stakes) × 0.20 × E(t)</span></td><td>Asignacion diaria de MIC del pool NFT Staking fusionado al holder i. 0.20 representa el 20% de la emision diaria asignada al pool NFT Staking fusionado. tier_mult: MFP-NFT ×10, Platinum ×5, Gold ×2.5, Silver ×1, No-NFT ×0.5.</td></tr>
<tr><td><span class="formula-math">VW<sub>Builder,i</sub> = S<sub>i</sub> / Σ S<sub>Builder,active</sub></span></td><td>Peso de voto del holder i de Builder NFT en votaciones comunitarias. Nivel base con multiplicador 1×, proporcional al MIC staked entre todos los Builders activos.</td></tr>
<tr><td><span class="formula-math">VW<sub>Maker,i</sub> = (S<sub>i</sub> × 2) / Σ weighted stakes</span></td><td>Peso de voto del holder i de Maker NFT en votaciones comunitarias conjuntas. Cada MIC staked por un Maker cuenta con multiplicador 2× dentro del total de weighted stakes.</td></tr>
<tr><td><span class="formula-math">VW<sub>Luminary,i</sub> = (S<sub>i</sub> × 4) / Σ weighted stakes</span></td><td>Peso de voto del holder i de Luminary NFT. Es el peso mas alto del nivel comunitario, con multiplicador 4×.</td></tr>
<tr><td><span class="formula-math">PS<sub>i</sub>(t) = (S<sub>i</sub> / Σ S<sub>Community,active</sub>) × tier_mult × 0.20 × E(t)</span></td><td>Participacion diaria del pool NFT Staking fusionado para el holder i. tier_mult es el multiplicador por nivel (Builder 1×, Maker 2×, Luminary 4×, o ajuste aprobado por governance).</td></tr>
</tbody></table></div>
<div class="callout gold">
<h3 class="sub-title">Por que las formulas no se traducen</h3>
<p>Las formulas matematicas son especificaciones tecnicas exactas, no prosa. Cambiar nombres de variables, notacion o formato numerico altera el significado de la formula y puede causar errores de implementacion, auditoria o comunicacion.</p>
</div>
<div class="callout">
<h3 class="sub-title">Referencia rapida</h3>
<p>Estos grupos deben permanecer en ingles en todas las traducciones y localizaciones de Mission Chain.</p>
<div class="quick-grid">
<div class="quick-card"><h3>Nombres de ecosistema y producto</h3><p>Mission Chain · Mission Chain Network · Mission DAO · Creator Mission Economy · Mission Network · Mission Network Layer 2 · Mission Learn · Mission Work · Mission Social · Mission Arts · Mission Hub · Mission Social Festival</p></div>
<div class="quick-card"><h3>Instrumentos economicos</h3><p>MIC · Mission Chain Token · MICE · Mission Algorithm Node License · MFP-NFT · Mission Founding Partner NFT · Community NFT · Builder NFT · Maker NFT · Luminary NFT · USDT</p></div>
<div class="quick-card"><h3>Terminos tecnicos y de governance</h3><p>DAO · NFT · Token · Staking / Stake / Staked · Smart Contract · Escrow · Hindex Algorithm · TWAP · DEX · Vesting · Cliff · TGE · Timelock · Quorum · Buy & Burn · Liquidity · Layer 2 · Multi-sig · On-chain · Off-chain · Mainnet · Testnet · BSC</p></div>
<div class="quick-card"><h3>Roles y programas comunitarios</h3><p>Hub Leader · Founding Member · Constitutional Steward · Active Steward · Honorary Steward · Legacy Credential · Founding Steward · Economic Oracle · Builder · Maker · Luminary · Global South · Creator Economy</p></div>
<div class="quick-card"><h3>Terminos de plataforma y negocio</h3><p>Portfolio · Dashboard · KPI · Roadmap · Flywheel · White Paper · MVP · ARR · Whitelist · Airdrop</p></div>
<div class="quick-card"><h3>Todas las variables de formula</h3><p>E(t) · E<sub>base</sub> · D(t) · L(t) · TWAP<sub>7d</sub> · L<sub>ref</sub> · L<sub>min</sub> · L<sub>max</sub> · R<sub>MICE,i</sub>(t) · VotingWeight<sub>MFP,i</sub> · PoolShare<sub>MFP,i</sub>(t) · VW<sub>Builder,i</sub> · VW<sub>Maker,i</sub> · VW<sub>Luminary,i</sub> · PS<sub>i</sub>(t)</p></div>
</div>
</div>
</section>
""".strip(),
    "pt": """
<section class="section anim a1" id="math">
<div class="section-num">Secao 7</div>
<h2 class="section-title">Variaveis de Formulas Matematicas</h2>
<p>Todas as formulas matematicas, nomes de variaveis, notacao funcional e constantes numericas nos documentos da Mission Chain devem permanecer exatamente como escritas em ingles, sem localizacao de simbolos, separadores ou notacao.</p>
<p>A Mission Chain usa ponto (.) como separador decimal internacional em todas as formulas, por exemplo 0.60, 0.95 e 22,907,500. Nao substitua esses valores por virgulas ou convencoes numericas locais dentro da sintaxe de formula.</p>
<div class="wp-table-wrap"><table class="wp-table formula-table"><thead><tr><th>Formula / Variavel</th><th>Definicao / Significado de cada variavel</th></tr></thead><tbody>
<tr><td><span class="formula-math">E(t) = E<sub>base</sub> × B × D(t) × L(t)</span></td><td>Formula diaria de emissao de MIC. t e o numero de dias decorridos desde a genesis do ecossistema. Os quatro componentes se multiplicam para produzir E(t), a emissao total de MIC liberada para a rede no dia t.</td></tr>
<tr><td><span class="formula-math">E₀ ≈ 22,907,500 MIC/day</span></td><td>Taxa inicial de emissao diaria sob o Adaptive Emission Engine. Combinada com decay exponencial (T_half = 180 dias), distribui exatamente 5,950,000,000 MIC (85% do suprimento total) ao pool de mineracao.</td></tr>
<tr><td><span class="formula-math">D(t) = 0.5 + U(t)</span></td><td>Fator de demanda. U(t) = taxa de utilizacao de MICE. Intervalo [0.5, 1.5]. Ajusta a emissao com base na demanda.</td></tr>
<tr><td><span class="formula-math">R(t) = clamp(250%/ROI, 0.5, 2.0)</span></td><td>Regulador de ROI. ROI alvo = 250%. Limitado entre 0.5 e 2.0.</td></tr>
<tr><td><span class="formula-math">R<sub>MICE,i</sub>(t) = (M<sub>i</sub> / N<sub>t</sub>) × 0.60 × E(t)</span></td><td>Recompensa diaria de MIC do operador MICE i no dia t. M<sub>i</sub> e o numero de licencas MICE ativas do operador i. N<sub>t</sub> e o total de licencas MICE ativas na rede. 0.60 representa 60% da emissao diaria destinada ao pool Miners.</td></tr>
<tr><td><span class="formula-math">VotingWeight<sub>MFP,i</sub> = S<sub>i</sub> / Σ S<sub>MFP,active</sub></span></td><td>Peso de voto do holder i de MFP-NFT. S<sub>i</sub> e o MIC em staking do holder i. Σ S<sub>MFP,active</sub> e a soma do MIC em staking de todos os holders ativos de MFP.</td></tr>
<tr><td><span class="formula-math">PoolShare<sub>NFT,i</sub>(t) = (S<sub>i</sub> × tier_mult / Σ weighted_stakes) × 0.20 × E(t)</span></td><td>Alocacao diaria de MIC do pool NFT Staking fusionado para o holder i. 0.20 representa 20% da emissao diaria destinada ao pool NFT Staking fusionado. tier_mult: MFP-NFT ×10, Platinum ×5, Gold ×2.5, Silver ×1, No-NFT ×0.5.</td></tr>
<tr><td><span class="formula-math">VW<sub>Builder,i</sub> = S<sub>i</sub> / Σ S<sub>Builder,active</sub></span></td><td>Peso de voto do holder i de Builder NFT nas votacoes comunitarias. Nivel base com multiplicador 1×, proporcional ao MIC em staking entre todos os Builders ativos.</td></tr>
<tr><td><span class="formula-math">VW<sub>Maker,i</sub> = (S<sub>i</sub> × 2) / Σ weighted stakes</span></td><td>Peso de voto do holder i de Maker NFT nas votacoes comunitarias conjuntas. Cada MIC em staking de um Maker conta com multiplicador 2× dentro do total de weighted stakes.</td></tr>
<tr><td><span class="formula-math">VW<sub>Luminary,i</sub> = (S<sub>i</sub> × 4) / Σ weighted stakes</span></td><td>Peso de voto do holder i de Luminary NFT. E o peso mais alto do nivel comunitario, com multiplicador 4×.</td></tr>
<tr><td><span class="formula-math">PS<sub>i</sub>(t) = (S<sub>i</sub> / Σ S<sub>Community,active</sub>) × tier_mult × 0.20 × E(t)</span></td><td>Participacao diaria do pool NFT Staking fusionado para o holder i. tier_mult e o multiplicador por nivel (Builder 1×, Maker 2×, Luminary 4×, ou ajuste aprovado por governance).</td></tr>
</tbody></table></div>
<div class="callout gold">
<h3 class="sub-title">Por que as formulas nao devem ser traduzidas</h3>
<p>Formulas matematicas sao especificacoes tecnicas exatas, nao prosa. Alterar nomes de variaveis, notacao ou formato numerico muda o significado da formula e pode causar erros de implementacao, auditoria ou comunicacao.</p>
</div>
<div class="callout">
<h3 class="sub-title">Referencia rapida</h3>
<p>Os grupos abaixo devem permanecer em ingles em todas as traducoes e localizacoes da Mission Chain.</p>
<div class="quick-grid">
<div class="quick-card"><h3>Nomes de ecossistema e produto</h3><p>Mission Chain · Mission Chain Network · Mission DAO · Creator Mission Economy · Mission Network · Mission Network Layer 2 · Mission Learn · Mission Work · Mission Social · Mission Arts · Mission Hub · Mission Social Festival</p></div>
<div class="quick-card"><h3>Instrumentos economicos</h3><p>MIC · Mission Chain Token · MICE · Mission Algorithm Node License · MFP-NFT · Mission Founding Partner NFT · Community NFT · Builder NFT · Maker NFT · Luminary NFT · USDT</p></div>
<div class="quick-card"><h3>Termos tecnicos e de governance</h3><p>DAO · NFT · Token · Staking / Stake / Staked · Smart Contract · Escrow · Hindex Algorithm · TWAP · DEX · Vesting · Cliff · TGE · Timelock · Quorum · Buy & Burn · Liquidity · Layer 2 · Multi-sig · On-chain · Off-chain · Mainnet · Testnet · BSC</p></div>
<div class="quick-card"><h3>Papeis e programas comunitarios</h3><p>Hub Leader · Founding Member · Constitutional Steward · Active Steward · Honorary Steward · Legacy Credential · Founding Steward · Economic Oracle · Builder · Maker · Luminary · Global South · Creator Economy</p></div>
<div class="quick-card"><h3>Termos de plataforma e negocio</h3><p>Portfolio · Dashboard · KPI · Roadmap · Flywheel · White Paper · MVP · ARR · Whitelist · Airdrop</p></div>
<div class="quick-card"><h3>Todas as variaveis de formula</h3><p>E(t) · E<sub>base</sub> · D(t) · L(t) · TWAP<sub>7d</sub> · L<sub>ref</sub> · L<sub>min</sub> · L<sub>max</sub> · R<sub>MICE,i</sub>(t) · VotingWeight<sub>MFP,i</sub> · PoolShare<sub>MFP,i</sub>(t) · VW<sub>Builder,i</sub> · VW<sub>Maker,i</sub> · VW<sub>Luminary,i</sub> · PS<sub>i</sub>(t)</p></div>
</div>
</div>
</section>
""".strip(),
    "ko": """
<section class="section anim a1" id="math">
<div class="section-num">Section 7</div>
<h2 class="section-title">Formula Variables</h2>
<p>Mission Chain 문서의 모든 수식, 변수명, 함수 표기, 수치 상수는 영어 원문 그대로 유지해야 합니다. 기호, 구분자, 표기법을 현지화하면 안 됩니다.</p>
<p>Mission Chain은 모든 수식에서 국제 표준인 점 (.) 을 소수점 구분자로 사용합니다. 예: 0.60, 0.95, 22,907,500. 수식 안에서는 쉼표나 현지 숫자 표기를 사용하지 마십시오.</p>
<div class="wp-table-wrap"><table class="wp-table formula-table"><thead><tr><th>Formula / Variable</th><th>Definition / Meaning of each variable</th></tr></thead><tbody>
<tr><td><span class="formula-math">E(t) = E<sub>base</sub> × B × D(t) × L(t)</span></td><td>MIC 일일 emission formula 입니다. t는 ecosystem genesis 이후 경과한 일수입니다. 네 구성요소를 곱해 day t의 총 MIC emission 인 E(t)를 계산합니다.</td></tr>
<tr><td><span class="formula-math">E₀ ≈ 22,907,500 MIC/day</span></td><td>Adaptive Emission Engine 하에서의 초기 일일 emission rate 입니다. 지수 decay (T_half = 180 일)와 결합하면 총 정확히 5,950,000,000 MIC (총 공급의 85%)를 mining pool에 배분합니다.</td></tr>
<tr><td><span class="formula-math">D(t) = 0.5 + U(t)</span></td><td>수요 인자. U(t) = MICE 이용률. 범위 [0.5, 1.5]. 수요에 따라 emission을 조정합니다.</td></tr>
<tr><td><span class="formula-math">R(t) = clamp(250%/ROI, 0.5, 2.0)</span></td><td>ROI 조절기. 목표 ROI = 250%. 0.5에서 2.0 사이로 제한됩니다.</td></tr>
<tr><td><span class="formula-math">R<sub>MICE,i</sub>(t) = (M<sub>i</sub> / N<sub>t</sub>) × 0.60 × E(t)</span></td><td>day t 에서 MICE operator i 의 일일 MIC reward 입니다. M<sub>i</sub> 는 operator i 가 보유한 active MICE license 수이고, N<sub>t</sub> 는 network 전체 active MICE license 총량입니다.</td></tr>
<tr><td><span class="formula-math">VotingWeight<sub>MFP,i</sub> = S<sub>i</sub> / Σ S<sub>MFP,active</sub></span></td><td>MFP-NFT holder i 의 voting weight 입니다. S<sub>i</sub> 는 holder i 의 MIC staked amount 이고, Σ S<sub>MFP,active</sub> 는 모든 active MFP holder 의 총 staking 입니다.</td></tr>
<tr><td><span class="formula-math">PoolShare<sub>NFT,i</sub>(t) = (S<sub>i</sub> × tier_mult / Σ weighted_stakes) × 0.20 × E(t)</span></td><td>NFT holder i 의 일일 NFT Staking Pool allocation 입니다. 0.20 은 daily emission 중 20%가 merged NFT Staking pool 에 배정됨을 뜻합니다. tier_mult: MFP-NFT ×10, Platinum ×5, Gold ×2.5, Silver ×1, No-NFT ×0.5.</td></tr>
<tr><td><span class="formula-math">VW<sub>Builder,i</sub> = S<sub>i</sub> / Σ S<sub>Builder,active</sub></span></td><td>Builder NFT holder i 의 community governance voting weight 입니다. 기본 레벨이며 1× multiplier 를 가집니다.</td></tr>
<tr><td><span class="formula-math">VW<sub>Maker,i</sub> = (S<sub>i</sub> × 2) / Σ weighted stakes</span></td><td>Maker NFT holder i 의 공동 community voting weight 입니다. Maker 의 staking MIC 는 total weighted stakes 안에서 2× 로 계산됩니다.</td></tr>
<tr><td><span class="formula-math">VW<sub>Luminary,i</sub> = (S<sub>i</sub> × 4) / Σ weighted stakes</span></td><td>Luminary NFT holder i 의 voting weight 입니다. community governance tier 에서 가장 높은 4× multiplier 를 가집니다.</td></tr>
<tr><td><span class="formula-math">PS<sub>i</sub>(t) = (S<sub>i</sub> / Σ S<sub>Community,active</sub>) × tier_mult × 0.20 × E(t)</span></td><td>holder i 의 NFT Staking merged pool daily share 입니다. tier_mult 는 Builder 1×, Maker 2×, Luminary 4× 의 tier multiplier 를 의미합니다.</td></tr>
</tbody></table></div>
<div class="callout gold">
<h3 class="sub-title">Why formulas must not be translated</h3>
<p>수식은 설명 문장이 아니라 정밀한 technical specification 입니다. 변수명, 표기법, 숫자 형식을 바꾸면 formula meaning 이 바뀌고 implementation, audit, communication 오류를 만들 수 있습니다.</p>
</div>
<div class="callout">
<h3 class="sub-title">Quick Reference</h3>
<p>아래 그룹은 모든 Mission Chain 번역본에서 영어 원문 그대로 유지해야 합니다.</p>
<div class="quick-grid">
<div class="quick-card"><h3>Ecosystem and product names</h3><p>Mission Chain · Mission Chain Network · Mission DAO · Creator Mission Economy · Mission Network · Mission Network Layer 2 · Mission Learn · Mission Work · Mission Social · Mission Arts · Mission Hub · Mission Social Festival</p></div>
<div class="quick-card"><h3>Economic instruments</h3><p>MIC · Mission Chain Token · MICE · Mission Algorithm Node License · MFP-NFT · Mission Founding Partner NFT · Community NFT · Builder NFT · Maker NFT · Luminary NFT · USDT</p></div>
<div class="quick-card"><h3>Technical and governance terms</h3><p>DAO · NFT · Token · Staking / Stake / Staked · Smart Contract · Escrow · Hindex Algorithm · TWAP · DEX · Vesting · Cliff · TGE · Timelock · Quorum · Buy & Burn · Liquidity · Layer 2 · Multi-sig · On-chain · Off-chain · Mainnet · Testnet · BSC</p></div>
<div class="quick-card"><h3>Community roles and programs</h3><p>Hub Leader · Founding Member · Constitutional Steward · Active Steward · Honorary Steward · Legacy Credential · Founding Steward · Economic Oracle · Builder · Maker · Luminary · Global South · Creator Economy</p></div>
<div class="quick-card"><h3>Platform and business terms</h3><p>Portfolio · Dashboard · KPI · Roadmap · Flywheel · White Paper · MVP · ARR · Whitelist · Airdrop</p></div>
<div class="quick-card"><h3>All formula variables</h3><p>E(t) · E<sub>base</sub> · D(t) · L(t) · TWAP<sub>7d</sub> · L<sub>ref</sub> · L<sub>min</sub> · L<sub>max</sub> · R<sub>MICE,i</sub>(t) · VotingWeight<sub>MFP,i</sub> · PoolShare<sub>MFP,i</sub>(t) · VW<sub>Builder,i</sub> · VW<sub>Maker,i</sub> · VW<sub>Luminary,i</sub> · PS<sub>i</sub>(t)</p></div>
</div>
</div>
</section>
""".strip(),
    "vi": """
<section class="section anim a1" id="math">
<div class="section-num">Muc 7</div>
<h2 class="section-title">Bien trong Cong thuc Toan hoc</h2>
<p>Tat ca cong thuc toan hoc, ten bien, ky hieu ham va hang so trong tai lieu Mission Chain phai duoc giu nguyen dung nhu ban tieng Anh, khong duoc dia phuong hoa ky hieu, dau phan cach hay notations.</p>
<p>Mission Chain su dung dau cham (.) lam dau thap phan theo chuan quoc te trong tat ca cong thuc, vi du 0.60, 0.95 va 22,907,500. Khong thay bang dau phay hoac quy uoc so dia phuong ben trong cu phap cong thuc.</p>
<div class="wp-table-wrap"><table class="wp-table formula-table"><thead><tr><th>Cong thuc / Bien</th><th>Dinh nghia / Y nghia cua tung bien</th></tr></thead><tbody>
<tr><td><span class="formula-math">E(t) = E<sub>base</sub> × B × D(t) × L(t)</span></td><td>Cong thuc phat thai MIC hang ngay. t la so ngay da troi qua ke tu genesis cua he sinh thai. Bon thanh phan duoc nhan voi nhau de tao ra E(t), tong MIC duoc phat hanh vao mang o ngay t.</td></tr>
<tr><td><span class="formula-math">E₀ ≈ 22,907,500 MIC/day</span></td><td>Muc phat thai ban dau theo Adaptive Emission Engine. Ket hop voi exponential decay (T_half = 180 ngay), muc nay se phan bo chinh xac 5,950,000,000 MIC (85% tong cung) vao mining pool.</td></tr>
<tr><td><span class="formula-math">D(t) = 0.5 + U(t)</span></td><td>He so nhu cau. U(t) = ty le su dung MICE. Pham vi [0.5, 1.5]. Dieu chinh emission dua tren nhu cau.</td></tr>
<tr><td><span class="formula-math">R(t) = clamp(250%/ROI, 0.5, 2.0)</span></td><td>Bo dieu chinh ROI. ROI muc tieu = 250%. Gioi han giua 0.5 va 2.0.</td></tr>
<tr><td><span class="formula-math">R<sub>MICE,i</sub>(t) = (M<sub>i</sub> / N<sub>t</sub>) × 0.60 × E(t)</span></td><td>Phan thuong MIC hang ngay cua MICE operator i tai ngay t. M<sub>i</sub> la so license MICE dang hoat dong cua operator i. N<sub>t</sub> la tong so license MICE dang hoat dong tren toan mang. 0.60 la 60% daily emission duoc phan bo cho pool Miners.</td></tr>
<tr><td><span class="formula-math">VotingWeight<sub>MFP,i</sub> = S<sub>i</sub> / Σ S<sub>MFP,active</sub></span></td><td>Trong so bo phieu cua holder MFP-NFT i. S<sub>i</sub> la luong MIC duoc staking boi holder i. Σ S<sub>MFP,active</sub> la tong MIC staking cua tat ca holder MFP dang active.</td></tr>
<tr><td><span class="formula-math">PoolShare<sub>NFT,i</sub>(t) = (S<sub>i</sub> × tier_mult / Σ weighted_stakes) × 0.20 × E(t)</span></td><td>Phan bo MIC hang ngay tu merged NFT Staking pool cho holder i. 0.20 bieu thi 20% daily emission duoc danh cho pool NFT Staking merged. tier_mult: MFP-NFT ×10, Platinum ×5, Gold ×2.5, Silver ×1, No-NFT ×0.5.</td></tr>
<tr><td><span class="formula-math">VW<sub>Builder,i</sub> = S<sub>i</sub> / Σ S<sub>Builder,active</sub></span></td><td>Trong so bo phieu cua Builder NFT holder i trong governance cap cong dong. Day la cap co so voi he so 1×.</td></tr>
<tr><td><span class="formula-math">VW<sub>Maker,i</sub> = (S<sub>i</sub> × 2) / Σ weighted stakes</span></td><td>Trong so bo phieu cua Maker NFT holder i trong bo phieu cong dong tong hop. MIC staking cua Maker duoc tinh voi he so 2× trong tong weighted stakes.</td></tr>
<tr><td><span class="formula-math">VW<sub>Luminary,i</sub> = (S<sub>i</sub> × 4) / Σ weighted stakes</span></td><td>Trong so bo phieu cua Luminary NFT holder i. Day la trong so cao nhat trong tier governance cong dong, voi he so 4×.</td></tr>
<tr><td><span class="formula-math">PS<sub>i</sub>(t) = (S<sub>i</sub> / Σ S<sub>Community,active</sub>) × tier_mult × 0.20 × E(t)</span></td><td>Phan chia pool NFT Staking merged hang ngay cho holder i. tier_mult la he so theo cap (Builder 1×, Maker 2×, Luminary 4×, hoac dieu chinh phe duyet boi governance).</td></tr>
</tbody></table></div>
<div class="callout gold">
<h3 class="sub-title">Vi sao cong thuc khong duoc dich</h3>
<p>Cong thuc toan hoc la cac dac ta ky thuat chinh xac, khong phai van xuoi. Neu doi ten bien, ky hieu hoac cach viet so, y nghia cua cong thuc se thay doi va co the gay loi trong implementation, audit va truyen thong.</p>
</div>
<div class="callout">
<h3 class="sub-title">Tham khao nhanh</h3>
<p>Cac nhom sau phai duoc giu nguyen bang tieng Anh trong moi ban dich va localize cua Mission Chain.</p>
<div class="quick-grid">
<div class="quick-card"><h3>Ten he sinh thai va san pham</h3><p>Mission Chain · Mission Chain Network · Mission DAO · Creator Mission Economy · Mission Network · Mission Network Layer 2 · Mission Learn · Mission Work · Mission Social · Mission Arts · Mission Hub · Mission Social Festival</p></div>
<div class="quick-card"><h3>Cong cu kinh te</h3><p>MIC · Mission Chain Token · MICE · Mission Algorithm Node License · MFP-NFT · Mission Founding Partner NFT · Community NFT · Builder NFT · Maker NFT · Luminary NFT · USDT</p></div>
<div class="quick-card"><h3>Thuat ngu ky thuat va governance</h3><p>DAO · NFT · Token · Staking / Stake / Staked · Smart Contract · Escrow · Hindex Algorithm · TWAP · DEX · Vesting · Cliff · TGE · Timelock · Quorum · Buy & Burn · Liquidity · Layer 2 · Multi-sig · On-chain · Off-chain · Mainnet · Testnet · BSC</p></div>
<div class="quick-card"><h3>Vai tro va chuong trinh cong dong</h3><p>Hub Leader · Founding Member · Constitutional Steward · Active Steward · Honorary Steward · Legacy Credential · Founding Steward · Economic Oracle · Builder · Maker · Luminary · Global South · Creator Economy</p></div>
<div class="quick-card"><h3>Thuat ngu nen tang va kinh doanh</h3><p>Portfolio · Dashboard · KPI · Roadmap · Flywheel · White Paper · MVP · ARR · Whitelist · Airdrop</p></div>
<div class="quick-card"><h3>Tat ca bien cong thuc</h3><p>E(t) · E<sub>base</sub> · D(t) · L(t) · TWAP<sub>7d</sub> · L<sub>ref</sub> · L<sub>min</sub> · L<sub>max</sub> · R<sub>MICE,i</sub>(t) · VotingWeight<sub>MFP,i</sub> · PoolShare<sub>MFP,i</sub>(t) · VW<sub>Builder,i</sub> · VW<sub>Maker,i</sub> · VW<sub>Luminary,i</sub> · PS<sub>i</sub>(t)</p></div>
</div>
</div>
</section>
""".strip(),
}


def replace_once(text: str, old: str, new: str, path: Path) -> str:
    if old not in text:
        raise RuntimeError(f"Missing expected snippet in {path}")
    return text.replace(old, new, 1)


def write(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")


def patch_index(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    if "function syncLandingLanguageMenu()" in text:
        write(path, text)
        return
    pattern = re.compile(r"function setLang\(lang, label, el\) \{.*?\n  \}\n\n  function setTheme", re.S)
    replacement = f"""
{ROUTE_HELPER}
  function syncLandingLanguageMenu() {{
    var currentLocale = detectLocale();
    var selected = document.getElementById('langSelected');
    if (selected) selected.textContent = LOCALE_LABELS[currentLocale] || LOCALE_LABELS.en;
    document.querySelectorAll('.lang-option').forEach(function(option) {{
      option.classList.toggle('active', option.textContent.trim() === (LOCALE_LABELS[currentLocale] || LOCALE_LABELS.en));
    }});
  }}

  function setLang(lang, label, el) {{
    document.getElementById('langSelected').textContent = label || LOCALE_LABELS[lang] || LOCALE_LABELS.en;
    document.querySelectorAll('.lang-option').forEach(function(o) {{ o.classList.remove('active'); }});
    if (el) el.classList.add('active');
    document.getElementById('langSwitcher').classList.remove('open');
    window.location.href = getLocalizedHref(lang, 'index.html');
  }}

  syncLandingLanguageMenu();

  function setTheme"""
    text, count = pattern.subn(replacement, text, count=1)
    if count != 1:
        raise RuntimeError(f"Could not patch index lang block in {path}")
    write(path, text)


def patch_whitepaper(path: Path, locale: str) -> None:
    text = path.read_text(encoding="utf-8")
    if "function syncWhitePaperLanguageButtons()" not in text:
        pattern = re.compile(r"let curLang = 'en';\nconst THEME_KEY = 'missionchain-theme';\nfunction setLang\(lang\) \{.*?\n\}", re.S)
        replacement = f"""
{ROUTE_HELPER}
let curLang = detectLocale();
const THEME_KEY = 'missionchain-theme';
function syncWhitePaperLanguageButtons() {{
  document.querySelectorAll('[id^="lb-"]').forEach(btn => btn.classList.remove('active'));
  const active = document.getElementById('lb-' + curLang);
  if (active) active.classList.add('active');
  document.documentElement.lang = curLang;
}}
function setLang(lang) {{
  curLang = lang;
  syncWhitePaperLanguageButtons();
  window.location.href = getLocalizedHref(lang, 'White_Paper.html');
}}
""".strip()
        text, count = pattern.subn(replacement, text, count=1)
        if count != 1:
            raise RuntimeError(f"Could not patch white paper lang block in {path}")
        text = replace_once(text, "setTheme(localStorage.getItem(THEME_KEY) || 'daylight');", "syncWhitePaperLanguageButtons();\nsetTheme(localStorage.getItem(THEME_KEY) || 'daylight');", path)
    if locale in WHITEPAPER_DOC_LINKS:
        website_label, glossary_label = WHITEPAPER_DOC_LINKS[locale]
        text = text.replace('href="index.html">Sitio web de la Misión</a>', f'href="index.html">{website_label}</a>')
        text = text.replace('href="index.html">Site da missão</a>', f'href="index.html">{website_label}</a>')
        text = text.replace('href="index.html">미션 웹사이트</a>', f'href="index.html">{website_label}</a>')
        text = text.replace('href="index.html">Trang web của Sứ mệnh</a>', f'href="index.html">{website_label}</a>')
        text = text.replace('href="Glossary_Brand_Terms.html">Glossary of Brand Terms</a>', f'href="Glossary_Brand_Terms.html">{glossary_label}</a>')
        for key, value in WHITEPAPER_APPENDIX[locale].items():
            text = re.sub(rf'(<button class="nav-link" data-t="nav-app{key}" onclick="goTo\(\'app{key}\'\)">)(.*?)(</button>)', rf'\1{value}\3', text)
    visible_replacements = {
        "es": {
            "× 0,60 ×": "× 0.60 ×",
            "0,95<sup>": "0.95<sup>",
            "22.907.500": "22,907,500",
            "Pinza[": "Clamp[",
            "MIC/día": "MIC/day",
            "MIC / día": "MIC / day",
            "Apéndice A - Ronda de siembra (venta privada para inversores iniciales y estratégicos)": "Apéndice A - Seed Round (Private Sale to Early and Strategic Investors)",
            "Apéndice B - Preventa": "Apéndice B - Pre-Sale",
            "Apéndice C - Estructura de venta MICE": "Apéndice C - Estructura de Venta de MICE",
            "Apéndice D - Espec Formal Económico": "Apéndice D - Especificacion Economica Formal",
            "VotingWeight<sub>MFP,i</sub> = S<sub>i</sub> / Σ S<sub>MFP,activo</sub>": "VotingWeight<sub>MFP,i</sub> = S<sub>i</sub> / Σ S<sub>MFP,active</sub>",
            "PoolShare<sub>NFT,i</sub>(t) = (S<sub>i</sub> × tier_mult / Σ weighted_stakes) × 0,20 × E(t)": "PoolShare<sub>NFT,i</sub>(t) = (S<sub>i</sub> × tier_mult / Σ weighted_stakes) × 0.20 × E(t)",
            "R<sub>COMM,i</sub>(t) = (S<sub>i</sub> / ΣS<sub>eff</sub>) × 0,20 × E(t)": "R<sub>COMM,i</sub>(t) = (S<sub>i</sub> / ΣS<sub>eff</sub>) × 0.20 × E(t)",
            "R<sub>NFT,i</sub>(t) = (S<sub>i</sub> × tier_mult / ΣS<sub>weighted</sub>) × 0,20 × E(t)": "R<sub>NFT,i</sub>(t) = (S<sub>i</sub> × tier_mult / ΣS<sub>weighted</sub>) × 0.20 × E(t)",
            "PS_NFT_i(t) = (S_i × tier_mult / Σ weighted_stakes) × 0,20 × E(t)": "PS_NFT_i(t) = (S_i × tier_mult / Σ weighted_stakes) × 0.20 × E(t)",
        },
        "pt": {
            "× 0,60 ×": "× 0.60 ×",
            "0,95<sup>": "0.95<sup>",
            "22.907.500": "22,907,500",
            "Grampo[": "Clamp[",
            "L<sub>máximo</sub>": "L<sub>max</sub>",
            "MIC/dia": "MIC/day",
            "MIC / dia": "MIC / day",
            "Apêndice A - Rodada de sementes (venda privada para investidores iniciais e estratégicos)": "Apêndice A - Seed Round (Private Sale to Early and Strategic Investors)",
            "Apêndice B - Pré-venda": "Apêndice B - Pre-Sale",
            "Apêndice C - Estrutura de venda MICE": "Apêndice C - Estrutura de Venda de MICE",
            "Apêndice D - Especificação formal econômica": "Apêndice D - Especificacao Economica Formal",
            "VotingWeight<sub>MFP,i</sub> = S<sub>i</sub> / Σ S<sub>MFP,ativo</sub>": "VotingWeight<sub>MFP,i</sub> = S<sub>i</sub> / Σ S<sub>MFP,active</sub>",
            "PoolShare<sub>NFT,i</sub>(t) = (S<sub>i</sub> × tier_mult / Σ weighted_stakes) × 0,20 × E(t)": "PoolShare<sub>NFT,i</sub>(t) = (S<sub>i</sub> × tier_mult / Σ weighted_stakes) × 0.20 × E(t)",
            "R<sub>COMM,i</sub>(t) = (S<sub>i</sub> / ΣS<sub>efeito</sub>) × 0,20 × E(t)": "R<sub>COMM,i</sub>(t) = (S<sub>i</sub> / ΣS<sub>eff</sub>) × 0.20 × E(t)",
            "R<sub>NFT,i</sub>(t) = (S<sub>i</sub> × tier_mult / ΣS<sub>weighted</sub>) × 0,20 × E(t)": "R<sub>NFT,i</sub>(t) = (S<sub>i</sub> × tier_mult / ΣS<sub>weighted</sub>) × 0.20 × E(t)",
            "PS_NFT_i(t) = (S_i × tier_mult / Σ weighted_stakes) × 0,20 × E(t)": "PS_NFT_i(t) = (S_i × tier_mult / Σ weighted_stakes) × 0.20 × E(t)",
        },
        "ko": {
            "클램프[": "Clamp[",
            "L<sub>분</sub>": "L<sub>min</sub>",
            "L<sub>최대</sub>": "L<sub>max</sub>",
            "부록 D - 경제적 공식 사양": "부록 D - 경제 공식 명세",
        },
        "vi": {
            "E<sub>cơ sở</sub>": "E<sub>base</sub>",
            "× 0,60 ×": "× 0.60 ×",
            "22.907.500": "22,907,500",
            "Kẹp [": "Clamp[",
            "L<sub>tham chiếu</sub>": "L<sub>ref</sub>",
            "L<sub>tối đa</sub>": "L<sub>max</sub>",
            "Phụ lục A — Vòng gọi vốn hạt giống (Bán cổ phần riêng lẻ cho các nhà đầu tư sớm và chiến lược)": "Phụ lục A — Seed Round (Private Sale to Early and Strategic Investors)",
            "Phụ lục B — Trước khi bán": "Phụ lục B — Pre-Sale",
            "Phụ lục C — Cấu trúc bán hàng MICE": "Phụ lục C — Cấu trúc Bán MICE",
            "Phụ lục D — Quy định kinh tế chính thức": "Phụ lục D — Đặc tả Kinh tế Chính thức",
            "Chia sẻ bể bơi<sub>NFT,i</sub>(t) = (S)<sub>i</sub> × tier_mult / Σ weighted_stakes) × 0,20 × E(t)": "PoolShare<sub>NFT,i</sub>(t) = (S<sub>i</sub> × tier_mult / Σ weighted_stakes) × 0.20 × E(t)",
            "R<sub>COMM,i</sub>(t) = (S)<sub>i</sub> / ΣS<sub>hiệu quả</sub>) × 0,20 × E(t)": "R<sub>COMM,i</sub>(t) = (S<sub>i</sub> / ΣS<sub>eff</sub>) × 0.20 × E(t)",
            "R<sub>NFT,i</sub>(t) = (S)<sub>i</sub> × tier_mult / ΣS<sub>weighted</sub>) × 0,20 × E(t)": "R<sub>NFT,i</sub>(t) = (S<sub>i</sub> × tier_mult / ΣS<sub>weighted</sub>) × 0.20 × E(t)",
            "S<sub>tối đa</sub>": "S<sub>max</sub>",
            "S<sub>khai thác</sub>": "S<sub>mining</sub>",
            "S<sub>trước</sub>": "S<sub>pre</sub>",
            "L<sub>tham khảo</sub>": "L<sub>ref</sub>",
        },
    }
    for old, new in visible_replacements.get(locale, {}).items():
        text = text.replace(old, new)
    write(path, text)


def build_glossary_bar(locale: str) -> str:
    website, whitepaper, glossary = GLOSSARY_TOP[locale]
    active = {k: (' active' if k == locale else '') for k in LOCALES}
    return f"""<div id=\"lang-bar\">\n  <div class=\"theme-toggle-group\" aria-label=\"Theme switcher\">\n    <button class=\"theme-btn active\" onclick=\"setTheme('daylight')\" id=\"theme-daylight\" aria-label=\"Daylight theme\">☀</button>\n    <button class=\"theme-btn\" onclick=\"setTheme('night')\" id=\"theme-night\" aria-label=\"Night theme\">☾</button>\n  </div>\n  <a class=\"top-btn\" href=\"index.html\">{website}</a>\n  <a class=\"top-btn\" href=\"White_Paper.html\">{whitepaper}</a>\n  <a class=\"top-btn active\" href=\"Glossary_Brand_Terms.html\">{glossary}</a>\n  <button class=\"top-btn{active['en']}\" onclick=\"setLang('en')\" id=\"lb-en\" type=\"button\">EN</button>\n  <button class=\"top-btn{active['es']}\" onclick=\"setLang('es')\" id=\"lb-es\" type=\"button\">ES</button>\n  <button class=\"top-btn{active['pt']}\" onclick=\"setLang('pt')\" id=\"lb-pt\" type=\"button\">PT</button>\n  <button class=\"top-btn{active['ko']}\" onclick=\"setLang('ko')\" id=\"lb-ko\" type=\"button\">한국어</button>\n  <button class=\"top-btn{active['vi']}\" onclick=\"setLang('vi')\" id=\"lb-vi\" type=\"button\">VI</button>\n</div>"""


def patch_glossary(path: Path, locale: str) -> None:
    text = path.read_text(encoding="utf-8")
    if "function syncGlossaryLanguageButtons()" not in text:
        pattern = re.compile(r'<div id="lang-bar">.*?</div>\n<button id="toggle-sb" onclick="toggleSidebar\(\)">☰</button>', re.S)
        replacement = build_glossary_bar(locale) + '\n<button id="toggle-sb" onclick="toggleSidebar()">☰</button>'
        text, count = pattern.subn(replacement, text, count=1)
        if count != 1:
            raise RuntimeError(f"Could not patch glossary lang bar in {path}")

        script_pattern = re.compile(r"const THEME_KEY = 'missionchain-theme';\nfunction setTheme\(theme\) \{", re.S)
        script_replacement = f"""
{ROUTE_HELPER}
const THEME_KEY = 'missionchain-theme';
function syncGlossaryLanguageButtons() {{
  const current = detectLocale();
  document.querySelectorAll('[id^="lb-"]').forEach(btn => btn.classList.remove('active'));
  const active = document.getElementById('lb-' + current);
  if (active) active.classList.add('active');
  document.documentElement.lang = current;
}}
function setLang(lang) {{
  window.location.href = getLocalizedHref(lang, 'Glossary_Brand_Terms.html');
}}
function setTheme(theme) {{""".strip()
        text, count = script_pattern.subn(script_replacement, text, count=1)
        if count != 1:
            raise RuntimeError(f"Could not patch glossary script in {path}")
        text = replace_once(text, "setTheme(localStorage.getItem(THEME_KEY) || 'daylight');", "syncGlossaryLanguageButtons();\nsetTheme(localStorage.getItem(THEME_KEY) || 'daylight');", path)

    if locale in GLOSSARY_DOC_LINKS:
        website_label, whitepaper_label = GLOSSARY_DOC_LINKS[locale]
        text = text.replace('href="index.html">Sitio web de la Misión</a>', f'href="index.html">{website_label}</a>')
        text = text.replace('href="index.html">Site da missão</a>', f'href="index.html">{website_label}</a>')
        text = text.replace('href="index.html">Trang web của Sứ mệnh</a>', f'href="index.html">{website_label}</a>')
        text = text.replace('href="index.html">Mission Website</a>', f'href="index.html">{website_label}</a>')
        text = text.replace('href="White_Paper.html">White Paper</a>', f'href="White_Paper.html">{whitepaper_label}</a>')

    replacements = {
        'Mission Chain Documentación': 'Documentacion de Mission Chain',
        'Condiciones de la marca': 'Terminos de Marca',
        'Glosario Mapa': 'Mapa del Glosario',
        'Instrumentos económicos y nombres Token': 'Instrumentos economicos y nombres de token',
        'Fórmula matemática Variables': 'Variables de Formulas Matematicas',
        '<th>Plazo</th>': '<th>Termino</th>',
        'Mission Chain Tài liệu': 'Tai lieu Mission Chain',
        'Điều khoản thương hiệu': 'Thuat ngu Thuong hieu',
        'tên Token': 'ten token',
        'Layer 2 Thương hiệu': 'Thuong hieu Layer 2',
        'Documentação Mission Chain': 'Documentacao Mission Chain',
        'Termos da marca': 'Termos da Marca',
        'nomes Token': 'nomes de token',
        'Variáveis da fórmula matemática': 'Variaveis de Formulas Matematicas',
        '<th>Prazo</th>': '<th>Termo</th>',
        '브랜드 약관': '브랜드 용어',
        '용어집 지도': '용어집 개요',
        'Token 이름': '토큰 명칭',
        '수학 공식 변수': 'Formula Variables',
        '<th>기간</th>': '<th>용어</th>',
    }
    for old, new in replacements.items():
        text = text.replace(old, new)

    quoted_term_replacements = {
        '"Misión"': '"Mission"',
        '"Cadena"': '"Chain"',
        '"Missão"': '"Mission"',
        '"미션"': '"Mission"',
        '"체인"': '"Chain"',
        '"Sứ mệnh"': '"Mission"',
    }
    for old, new in quoted_term_replacements.items():
        text = text.replace(old, new)

    if locale in GLOSSARY_FORMULA_BLOCKS:
        text, count = re.subn(r'<section class="section anim a1" id="math">.*?</section>', GLOSSARY_FORMULA_BLOCKS[locale], text, count=1, flags=re.S)
        if count != 1:
            raise RuntimeError(f"Could not replace glossary formula block in {path}")
    glossary_titles = {
        "es": "Glosario de Terminos de Marca",
        "pt": "Glossario de Termos da Marca",
        "ko": "브랜드 용어집",
        "vi": "Bang Thuat ngu Thuong hieu",
    }
    if locale in glossary_titles:
        title = glossary_titles[locale]
        text = text.replace('<div class="sidebar-logo-text">Mission Chain<span>Glossary of Brand Terms</span></div>', f'<div class="sidebar-logo-text">Mission Chain<span>{title}</span></div>')
        text = text.replace('<div class="foot-tagline">Glossary of Brand Terms</div>', f'<div class="foot-tagline">{title}</div>')
    write(path, text)


def patch_index_visible_content(path: Path, locale: str) -> None:
    text = path.read_text(encoding="utf-8")
    replacements = {
        "es": {
            "22.907.500": "22,907,500",
            "6,5": "6.5",
            "0,95<sup>": "0.95<sup>",
            "Pinza[": "Clamp[",
            "MIC/día": "MIC/day",
        },
        "pt": {
            "22.907.500": "22,907,500",
            "6,5": "6.5",
            "0,95<sup>": "0.95<sup>",
            "Grampo[": "Clamp[",
            "L<sub>máximo</sub>": "L<sub>max</sub>",
            "MIC/dia": "MIC/day",
        },
        "ko": {
            "클램프[": "Clamp[",
            "L<sub>분</sub>": "L<sub>min</sub>",
            "L<sub>최대</sub>": "L<sub>max</sub>",
        },
        "vi": {
            "E<sub>cơ sở</sub>": "E<sub>base</sub>",
            "22.907.500": "22,907,500",
            "6,5": "6.5",
            "0,95<sup>": "0.95<sup>",
            "Kẹp [": "Clamp[",
            "L<sub>tham chiếu</sub>": "L<sub>ref</sub>",
            "L<sub>tối đa</sub>": "L<sub>max</sub>",
        },
    }
    for old, new in replacements.get(locale, {}).items():
        text = text.replace(old, new)
    write(path, text)


def patch_seed_or_announcement(path: Path, kind: str) -> None:
    text = path.read_text(encoding='utf-8')
    if "function syncFormLanguageMenu()" not in text:
        if "var lang='en';" in text:
            text = replace_once(text, "var lang='en';", ROUTE_HELPER + "\nvar lang=detectLocale();", path)
        elif "var lang = 'en';" in text:
            text = replace_once(text, "var lang = 'en';", ROUTE_HELPER + "\nvar lang = detectLocale();", path)
        else:
            raise RuntimeError(f"Missing lang initializer in {path}")
    pattern = re.compile(r"function sl\(l,\s*label,\s*el\)\s*\{.*?\n\}", re.S)
    fallback = 'mc_seed_round.html' if kind == 'seed' else 'mc_announcement.html'
    replacement = f"""
function syncFormLanguageMenu() {{
  var current = detectLocale();
  document.getElementById('LSL').textContent = LOCALE_LABELS[current] || LOCALE_LABELS.en;
  document.querySelectorAll('.lopt').forEach(function(o) {{
    o.classList.toggle('on', o.textContent.trim() === (LOCALE_LABELS[current] || LOCALE_LABELS.en));
  }});
  document.documentElement.className = (current === 'en') ? '' : 'lang-' + current;
}}
function sl(l, label, el) {{
  document.getElementById('LSL').textContent = label || LOCALE_LABELS[l] || LOCALE_LABELS.en;
  document.querySelectorAll('.lopt').forEach(function(o) {{ o.classList.remove('on'); }});
  if (el) el.classList.add('on');
  document.getElementById('LS').classList.remove('open');
  window.location.href = getLocalizedHref(l, '{fallback}');
}}
""".strip()
    if "function syncFormLanguageMenu()" not in text:
        text, count = pattern.subn(replacement, text, count=1)
        if count != 1:
            raise RuntimeError(f"Could not patch form lang block in {path}")
        text = replace_once(text, "render();", "syncFormLanguageMenu();\nrender();", path)
    write(path, text)


def main() -> None:
    # Root English files
    patch_index(ROOT / 'index.html')
    patch_whitepaper(ROOT / 'White_Paper.html', 'en')
    patch_glossary(ROOT / 'Glossary_Brand_Terms.html', 'en')
    patch_seed_or_announcement(ROOT / 'mc_seed_round.html', 'seed')
    patch_seed_or_announcement(ROOT / 'mc_announcement.html', 'announcement')

    for locale in ['es', 'pt', 'ko', 'vi']:
        base = ROOT / 'translations' / locale
        patch_index(base / 'index.html')
        patch_index_visible_content(base / 'index.html', locale)
        patch_whitepaper(base / 'White_Paper.html', locale)
        patch_glossary(base / 'Glossary_Brand_Terms.html', locale)
        patch_seed_or_announcement(base / 'mc_seed_round.html', 'seed')
        patch_seed_or_announcement(base / 'mc_announcement.html', 'announcement')

if __name__ == '__main__':
    main()
