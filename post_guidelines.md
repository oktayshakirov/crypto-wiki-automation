# AI Post Writing Guidelines

## Structure (Flexible 5-8 Core Sections)

**Common Post Types:**

- **"What is..."** (Explanatory): Definition → How it works → Use cases → Conclusion
- **"How to..."** (Tutorial): Introduction → Step-by-step → Best practices → Conclusion
- **Educational/Topical**: Introduction → Main concepts → Examples → Practical considerations → Conclusion

**FLEXIBILITY**: Add contextual sections as needed (e.g., "Security Considerations", "Future Outlook", "Comparison with Alternatives").

For **"How to..."** and beginner-focused guides: Engaging introduction (2–3 paragraphs) → Why this matters → Core concepts → Step-by-step → Common mistakes/FAQs → Conclusion

## Content Requirements

- **Length**: 1,200-2,500 words
- **Internal Links**: 8-15 total, ALL using **[Text](/path)** bold format, flowing naturally
- **Images**: Exactly 2 with descriptive alt text using `/images/posts/` paths (first after main concept, second before conclusion)
- **Formatting**: ## for main headings, **bold** for ALL sub-categories in bullet points
- **Tone**: Professional, educational, expert-level, E-E-A-T compliant, accessible to beginners

## Content Structure & Flow

**CRITICAL: Prefer Narrative Prose Over Lists**

- Write in flowing narrative paragraphs that connect ideas naturally
- Use bullet points sparingly—only for 3-5 distinct items that benefit from visual separation
- When using bullets: Always introduce with narrative paragraph, follow with narrative that ties back
- Avoid list-heavy sections—convert multiple lists to prose

**Avoid Repetition**

- Don't explain the same concept in multiple sections—reference earlier explanations instead
- Each section should add new information, not restate what's already covered
- Review entire article before finalizing to eliminate redundancy

**Maintain Narrative Flow**

- Each paragraph should flow naturally to the next with clear transitions
- Guide readers through ideas in logical sequence
- Use transition sentences between major sections
- Article should read as unified narrative, not disconnected points

## ArticleAd Placement (MANDATORY)

**Format**: `<ArticleAd />` on its own line with blank lines above and below

**Placement Rules:**

- After complete sections only (never mid-section)
- Avoid image proximity (maintain at least one complete section between ads and images)
- Even distribution: 2-3 for <100 lines, 3-4 for 100-150 lines, 4-6 for 150+ lines
- Pattern: First ad after introduction, subsequent ads after major sections, last ad before final section

## Internal Linking (ALWAYS USE BOLD FORMAT)

**MANDATORY FORMAT**: **[Text](/path)** NOT [Text](/path)

**DO Link When:**

- Core concepts at first mention: "understanding **[Bitcoin](/posts/what-is-bitcoin)**"
- Related educational content: "our **[crypto for beginners](/posts/crypto-for-beginners)** guide"
- Technologies/protocols: "built on **[blockchain](/posts/what-is-blockchain)**"
- Exchanges when recommending: "purchase on **[Coinbase](/exchanges/coinbase)**"
- Crypto OGs when mentioned: "created by **[Vitalik Buterin](/crypto-ogs/vitalik-buterin)**"

**DON'T Link:**

- Every mention of common terms (only when it adds value)
- With forced phrases—let links flow naturally
- Multiple links in same sentence
- Repeated linking to same page (once per major section is enough)

**Link Validation:**

- ONLY use links from provided database (crypto_ogs, posts, exchanges, tools)
- Use exact slug from database: **[Title](/posts/{slug})** | **[Exchange](/exchanges/{slug})** | **[Name](/crypto-ogs/{slug})** | **[Tool](/tools/{slug})**

## Writing Standards

- **Capitalization (MANDATORY)**: Title Case every word in crypto OG and exchange names in body, JSON, and frontmatter (e.g. Satoshi Nakamoto, Nick Szabo). Never lowercase, slugs, or dot-keys like nick.szabo.
- **Specific Numbers & Data**: Use exact numbers "200+ cryptocurrencies", "99.9% reduction", "2,700-4,000 TPS" - AVOID vague terms like "many", "most", "several"
- **Historical Context**: Include founding years, launch dates, key events with dates
- **Risk Context**: Include naturally when discussing features (e.g., "While leverage can amplify profits, it also increases potential losses")
- **Balanced Tone**: Acknowledge strengths AND weaknesses objectively
- **Actionable Content**: Provide practical advice with context, explain "why" not just "what"
- **Natural Voice**: Vary sentence length, avoid AI-like filler ("In conclusion", "Furthermore" - use sparingly), write conversationally but professionally
- **Punctuation**: Avoid em-dash asides (`X—Y`); use spaced hyphen `X - Y` (reads less like generic AI).
- **Beginner-Friendly**: Explain technical terms on first use when concept is central, link to foundational content when appropriate. Make complex topics accessible without dumbing down.
- **Concrete Examples**: Include 2 short real-world scenarios or anonymized mini case studies (especially for security, scams, "how to", and risk topics)
- **Directly address reader**: Use "you"/"your" to acknowledge their concerns and goals
- **Use analogies**: Explain complex ideas with simple comparisons
- **Encouraging tone**: Combine honest risk discussion with reassurance, especially for beginners and security topics


## Available Body Images
Both body images use markdown format `![alt](/images/posts/FILENAME)` and MUST be chosen from this list (do NOT invent filenames; pick ones that fit the section). You may also use `/images/exchanges/{slug}.png` when featuring a specific exchange that exists in the DB.
ai-and-human.jpg,ai-human-hands.jpg,allianz.jpg,altcoins.jpg,analysis.jpg,apple.jpg,bear-market.png,binance-banner.png,binance-smart-chain.png,bitcoin-locked.jpg,bitcoin-mining.jpg,bitcoin-neon.jpg,bitcoin-renewable-energy.jpg,bitcoin-trading.jpg,bitcoin-vs-fiat.jpg,bitcoin-whitepaper.png,bitcoin-woman.jpg,bitcoin.jpg,bitfinex-ui.png,bitget-office.jpg,bitget-trading.jpg,bitpanda-app.png,bitpanda-banner.png,blockchain-technology.jpg,bored-ape-yacht-club.jpg,buying-bitcoin.jpg,cardano.png,chainlink.jpg,changpeng-zhao-2.png,changpeng-zhao.png,coinbase-app.jpg,coinbase-office.jpg,coinbase-wallet.png,coinex-exchange.png,coinex-logo.png,console-gaming.jpg,cookie-jar.jpg,corporate.jpg,couple-with-money.jpg,crypto-airdrop.jpg,crypto-banner.jpg,crypto-books.jpg,crypto-cards.png,crypto-exchange.jpg,crypto-exchange.webp,crypto-future.jpg,crypto-grandma.jpg,crypto-investing.jpg,crypto-staking.jpg,crypto-taxes.jpg,crypto-trade.jpg,crypto-transfer.jpg,cryptocurrency.jpg,data-center.jpg,defi.jpg,digital-technology.jpg,dogecoin.jpg,donald-trump.png,elon-musk.png,energy.jpg,ethereum-2.jpg,ethereum-network.jpg,ethereum.jpg,fear-and-greed-index.png,female-with-fiat-money.jpg,fiat-bitcoins.jpg,fiat-money.jpg,flag-el-salvador.jpg,ftx-collapse.jpg,futuristic-crypto-exchange.jpg,futuristic-data-center.jpg,futuristic-ui.jpg,gamers.jpg,gemini-exchange-hero.webp,gemini-exchange-trading.jpg,girl-with-money.jpg,global-map.jpg,gold.jpg,grand-theft-auto.jpg,greedy-investor-2.jpg,greedy-investor.jpg,hacker.jpg,hackers.jpg,htx-dashboard.jpg,industrial.jpg,investing.jpg,iphones.jpg,kucoin-exchange.jpg,kucoin-logo.png,laptop-trading.jpg,law.jpg,ledger.jpeg,lido-ethereum.png,litecoin.jpg,man-and-laptop.jpg,memecoins-meme.png,metaverse.jpg,mexc-interface.jpg,michael-saylor.png,mining-rig.jpg,nexo-exchange.jpg,nexo-swap.jpg,one-coin.jpeg,one-coin.jpg,polkadot.jpg,portfolio.jpg,proof-of-stake.jpg,proof-of-work.jpg,quantum-computing.png,real-estate.jpg,regulators.jpg,research.jpg,robot-human-hands-interacting.jpg,rugpull.jpg,satoshi-nakamoto.jpg,satoshi-nakamoto.png,scam.jpg,scammer.jpg,snoop-dogg-nfts.png,solana.jpeg,south-korean-flag.jpg,squid-game.jpg,stock-trader.jpg,suit-man-and-bitcoin.jpg,telegram.jpg,tesla.jpg,trade-republic-app.jpg,trading.jpg,tron.png,upbit-exchange-interface.webp,usa-trading.jpg,vitalik-buterin.jpg,vk.png,whitebit-logo.png,woman-browsing-internet.jpg,woman-buying-crypto.jpg

## Category Selection (MANDATORY - Use ONLY These Categories)

Choose 1-4 categories from this EXACT list: **Investing**, **Beginners**, **Regulation**, **Bitcoin**, **Adoption**, **Blockchain**, **Technology**, **Web3**, **Predictions**, **Security**, **Politics**, **Sustainability**, **Gaming**, **Nfts**, **Ai**

**Guidelines**: Choose 2-3 optimal categories, match to post's primary focus (not just mentioned terms), quality over quantity.

## Opening Style

**Requirements:**

- Start directly with a **## heading** (main topic heading), not introductory paragraphs before the first heading
- The first heading should introduce the topic (e.g., "## Understanding Cryptocurrency Volatility" or "## Essential Cryptocurrency Terms Explained")
- After the heading, begin with 2–3 short paragraphs that: use relatable scenarios/questions/historical context, acknowledge reader's situation, state what they'll learn, include ONE natural internal link

## Conclusion Style

- Every post MUST end with **Conclusion section** using heading `## Conclusion: [Short Benefit-Oriented Phrase]` or `## Conclusion`
- **2–3 paragraphs** (not bullet checklist)
- Summarize key takeaways in plain language, restate why topic matters
- Reinforce confidence that reader can act safely/make better decisions
- Suggest 1–2 practical next steps with natural internal links

## Frontmatter Requirements

**Title Formats:** "What is [Topic]?", "How to [Action]", "Understanding [Topic]", "[Topic]: [Subtitle]", or question format

**Question marks (MANDATORY):** If the title is a question, it MUST end with "?" - this is how every past article was built, so it is a consistency requirement, not a preference. Applies to interrogative openers: What / Why / Is / Are / Can / Should / Do / Does / Who / When / Where / Which (e.g. "What Is the Bitcoin Halving?", "Are NFTs Dead?"). It does NOT apply to instructional "How to [Action]" titles, which are directions rather than questions (e.g. "How to Buy Your First Cryptocurrency" stays as-is). When the title has a subtitle, the "?" goes on the question part, not the end: "What is Bitcoin? A Beginner's Guide".

**Description (CRITICAL - EXACTLY 150-160 characters):**

- VERY SPECIFIC with unique differentiators (NOT generic)
- Formula: [Topic name] + [Key features] + [What readers learn] + [Audience optional]
- ❌ BAD: "Learn about cryptocurrency and how it works"
- ✅ GOOD: "Bitcoin is the world's first cryptocurrency. Learn about its history, how it works, and why it's considered digital gold. Perfect for beginners looking to understand the foundation of the crypto world."

**Image**: `/images/posts/{descriptive-name}.jpg` or `.png`

**Categories**: Array of 1-4 from allowed list

**Crypto OGs (Optional)**: Only when founder/creator mentioned: `crypto-ogs: ["Satoshi Nakamoto", "Hal Finney"]` (same Title Case as body; see Capitalization above).

**Exchanges (Optional)**: Only when recommending services: `exchanges: ["Coinbase", "Binance"]` (Title Case; see Capitalization above).

## Content Restrictions

**DO NOT Include:**

- References section at the end
- Bibliography or citation lists
- External links to other websites (only use internal links from provided database)
- Closing sections that list related articles—links should be integrated naturally throughout

## Final JSON Output (REQUIRED)

After writing the post, provide JSON:

```json
{
  "description": "Bitcoin is the world's first cryptocurrency. Learn about its history, how it works, and why it's considered digital gold. Perfect for beginners looking to understand the foundation of the crypto world.",
  "categories": ["Beginners", "Technology", "Blockchain", "Bitcoin"],
  "crypto_ogs": ["Satoshi Nakamoto"],
  "exchanges": ["Coinbase", "Binance", "Kraken"]
}
```

**Requirements:**

- **Description**: EXACTLY 150-160 characters, SPECIFIC with unique differentiator
- **Categories**: 1-4 from allowed list
- **Crypto OGs/Exchanges**: Optional if relevant; Title Case display names (not slugs).

## Quality Checklist

**Structure**: Start with ## heading, engaging opening paragraphs after heading, all core sections with ## headers, conclusion (2-3 paragraphs), 1,200-2,500 words

**ArticleAd Placement**: 2-6 ads evenly distributed, after complete sections only, avoid image proximity, first after introduction, last before conclusion

**Links & Images**: 8-15 internal links using **[Text](/path)** bold format, exactly 2 images with descriptive alt text, paths use `/images/posts/`

**Content**: Specific numbers/data, historical context with dates, balanced tone, **bold** sub-categories, prose preferred, no repetition, narrative flow, `X - Y` not `X—Y` for asides
