# AI Exchange Review Guidelines

## Structure (7 Core Sections + ExchangeButton)

1. **## [Exchange]: [Specific Descriptor]** - Opening with founding year, founder(s) if notable, headquarters, 1-2 positioning sentences highlighting uniqueness
2. **## Core [Services/Offerings/Platform]** - Trading features, spot/derivatives/margin, staking, DeFi, specialized products
3. **## Security Measures** - Account security, platform security, historical incidents if any, custody arrangements
4. **## User Experience** - Interface, educational resources, customer support, onboarding
5. **## Regulatory Compliance** - Licenses, registrations, challenges, geographic restrictions
6. **## Points to Consider** - 4-5 specific actionable points: fees, complexity, target users, important considerations
7. **## Conclusion** - Market position, ideal users, balanced verdict sentence summarizing pros/cons
8. **ExchangeButton Component** (MANDATORY) - Add at the very end: `<ExchangeButton href="{website}" text="Join {Exchange Name}" />`

FLEXIBILITY: The 7 sections are MINIMUM. Add contextual sections as needed (e.g., "Founders and Historical Context", "Token Utility", "Proof of Reserves", "Brand Building"). Adapt section 2 header to exchange type.

## Content Requirements

- **Length**: 1,500-2,500 words
- **Internal Links**: 8-15 total, ALL using **[Text](/path)** bold format, flowing naturally
- **Images**: Exactly 2 with descriptive alt text using /images/posts/ paths
  - First: After Core Services, before Security
  - Second: After User Experience/Regulatory, before Conclusion
- **Formatting**: ## for main headings, **bold** for ALL sub-categories in bullet points
- **Tone**: Professional, balanced, expert-level, E-E-A-T compliant
- **SEO**: Include naturally 'cryptocurrency exchange', 'crypto trading', 'digital assets'

## Internal Linking (NATURAL FLOW - ALWAYS USE BOLD)

**MANDATORY FORMAT**: **[Text](/path)** NOT [Text](/path)

**Natural Linking Strategy (8-15 total links):**

**DO Link When:**

- **Exchange comparisons**: Use relevant exchanges from the database that make sense contextually (e.g., "compare with [Coinbase](/exchanges/coinbase) for US users" or "similar to [KuCoin](/exchanges/kucoin) for altcoin trading")
- **Core concepts in context**: "trading [Bitcoin](/posts/what-is-bitcoin) and [Ethereum](/posts/what-is-ethereum)"
- **Essential safety content**: "learn [how to store crypto](/posts/how-to-store-crypto) safely"
- **Educational opportunities**: "understanding [DeFi](/posts/what-is-defi) protocols"
- **Founders when relevant**: "founded by [Vitalik Buterin](/crypto-ogs/vitalik-buterin)"

**DON'T Link:**

- Every mention of common terms (blockchain, volatility, taxes, airdrops)
- With forced phrases like "see our guide on..." or "read more about..."
- Multiple links in the same sentence
- As keyword stuffing or SEO manipulation
- When it interrupts reading flow

**Link Validation Rules**:

- ONLY use links from the provided database (crypto_ogs, posts, exchanges, tools)
- Database format: `key|slug|title`
- Search database for relevant entries (e.g., "bitcoin", "ethereum", "defi", "staking", "nft")
- Check variations: "nft" vs "non-fungible tokens", "crypto scams" vs "scams", "store crypto" vs "storage"
- **Founders**: **[Name](/crypto-ogs/{slug})** - ONLY if name exists in crypto_ogs database
- **Exchanges**: **[Exchange](/exchanges/{slug})** - Use for comparisons (check exchanges database)
- **Concepts**: **[Title](/posts/{slug})** - Use exact slug from posts database
- **Tools**: **[Tool](/tools/{slug})** - Use exact slug from tools database

**Exchange Comparison Guidelines**:

- **Choose contextually relevant exchanges** from the database, not the same ones every time
- **Consider the exchange type**: CEX vs DEX, US-based vs global, specialized vs general
- **Match the context**: If discussing US compliance, mention US exchanges; if discussing altcoins, mention altcoin-focused exchanges
- **Use 1-2 exchanges maximum** per comparison to avoid clutter
- **Make comparisons meaningful**: "similar to [Coinbase](/exchanges/coinbase) for regulatory compliance" vs generic "compare with [Binance](/exchanges/binance)"

**GOAL**: Natural, helpful linking that enhances user experience without feeling intrusive. Links should feel like natural recommendations, not mandatory reading assignments.

## Writing Standards

- **Specific Numbers**: "200+ cryptocurrencies", "700+ trading pairs", "95%+ cold storage" (NOT "many" or "most")
- **Historical Context**: Include founding year, major incidents with dates, regulatory milestones
- **Risk Context**: Include relevant risk information naturally when discussing specific features (derivatives, custody, regulatory issues)
- **Balanced Tone**: Acknowledge strengths AND limitations objectively
- **Actionable Advice**: "Points to Consider" must be specific and useful
- **Natural Voice**: Avoid AI-like filler, vary sentence length, use occasional short sentences
- **Avoid Excessive Disclaimers**: Don't add generic risk warnings or legal disclaimers unless contextually relevant to specific features being discussed

## Opening Descriptor Examples

Choose positioning based on exchange type:

- "A Publicly Traded US-Based Crypto Exchange" (Coinbase)
- "A Global Leader in Cryptocurrency Services" (Binance)
- "A Global Hub for Altcoin Trading" (KuCoin)
- "The Pioneering Decentralized Exchange (DEX)" (Uniswap)
- "Korea's Dominant Fiat On-Ramp for Altcoin Trading" (Upbit)
- "A Deep Dive into Derivatives and Spot Trading" (Bybit)

## Section Header Variations

**Section 2 adapts to exchange type:**

- Standard CEX: "Core Offerings and Ecosystem", "Core Services", "Core Trading Platform"
- Multi-Product: "Core Components of the [Name] Ecosystem"
- Specialized: "Core Services: Borrowing, Earning, and Exchanging" (lending platforms)
- DEX: "Core Protocol: How [Name] Works"

**Section 5 variations:**

- "Regulatory Compliance"
- "Global Operations and Regulatory Landscape"
- "Regulatory Compliance and Licensing"
- "Decentralization and the Regulatory Landscape" (for DEX)

## Natural Risk Context

Include risk information naturally when relevant:

- **Derivatives**: When discussing leverage or derivatives, naturally mention risks: "While leverage can amplify profits, it also increases potential losses"
- **Custodial**: When discussing custody, mention considerations: "Users should consider self-custody for long-term storage"
- **Regulatory**: When discussing compliance, mention geographic considerations: "Availability varies by jurisdiction"
- **DEX Risks**: When discussing liquidity provision, mention impermanent loss naturally

## Bullet Point Structure

- **Main Category**: **Bold** with colon → **Trading Platform:**
- **Sub-categories**: **Bold** with details → **Spot Trading:** specific features and numbers
- ALWAYS use **bold** for ALL sub-categories consistently

## Final JSON Output (REQUIRED)

After writing review, provide JSON with social links AND description:

```json
{
  "social": {
    "website": "https://exchange.com",
    "twitter": "https://twitter.com/exchange",
    "youtube": "https://youtube.com/@exchange",
    "linkedin": "https://linkedin.com/company/exchange",
    "facebook": "https://facebook.com/exchange",
    "instagram": "https://instagram.com/exchange",
    "telegram": "https://t.me/exchange",
    "discord": "https://discord.gg/exchange",
    "reddit": "https://reddit.com/r/exchange",
    "tiktok": "https://tiktok.com/@exchange",
    "apple": "https://apps.apple.com/app/exchange",
    "android": "https://play.google.com/store/apps/details?id=com.exchange",
    "wikipedia": "https://en.wikipedia.org/wiki/Exchange"
  },
  "description": "Leading US-based crypto exchange offering secure trading, staking and educational resources"
}
```

**Requirements:**

- Minimum 5 social platforms (research official accounts only, quality over quantity)
- Description: 80-120 characters, SPECIFIC with unique differentiator (NOT generic)
- Required social: website, twitter, app stores (apple/android)

**Social Media Research Guidelines:**

- **Research official website** for actual social links (footer/header)
- **Only include verified URLs** - NO guessing or generic patterns
- **Quality over quantity**: 5 verified links > 10 broken ones
- **App stores**: Search "Download" or "App" sections

**Description Quality:**
❌ BAD: "comprehensive cryptocurrency trading services with advanced features"  
✅ GOOD: "Binance offers advanced trading services, staking, and DeFi opportunities, making it a global leader in crypto."  
✅ GOOD: "Crypto.com simplifies trading, staking and DeFi, bringing digital assets into your everyday life."

## Quality Checklist

Before finalizing:

**Structure**

- [ ] Opening: ## **[Exchange Name]: [Specific Descriptor]** (NOT "Brief Description")
- [ ] All 7 core sections present with ## headers
- [ ] Section 2 header adapted to exchange type
- [ ] Conclusion ends with verdict sentence

**Links (NATURAL FLOW)**

- [ ] 8-15 internal links flowing naturally with content
- [ ] ALL links use **[Text](/path)** bold format
- [ ] Links feel like natural recommendations, not forced assignments
- [ ] Exchange comparisons when relevant using contextually appropriate exchanges from database
- [ ] Core concepts linked in context (Bitcoin, Ethereum, DeFi, staking)
- [ ] Essential safety content linked naturally
- [ ] Verified all links exist in database (used exact keys)
- [ ] NO forced phrases like "see our guide on..." or "read more about..."

**Images**

- [ ] Exactly 2 images with descriptive alt text
- [ ] Paths use /images/posts/ (NOT /images/exchanges/)
- [ ] First: After Core Services, before Security
- [ ] Second: After User Experience/Regulatory, before Conclusion

**Content**

- [ ] 1,200+ words minimum
- [ ] Specific numbers throughout (e.g., "200+ cryptocurrencies")
- [ ] Risk information included naturally when relevant to specific features
- [ ] **Bold** formatting for ALL sub-categories
- [ ] Balanced tone (strengths AND limitations)
- [ ] ExchangeButton at the very end
- [ ] Description is 80-120 characters, specific and unique (not generic)
