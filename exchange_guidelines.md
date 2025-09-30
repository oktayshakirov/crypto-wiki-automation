# AI Exchange Review Guidelines

## Structure (7 Core Sections + ExchangeButton)

1. **## [Exchange]: [Specific Descriptor]** - Opening with founding year, founder(s) if notable, headquarters, 1-2 positioning sentences highlighting uniqueness
2. **## Core [Services/Offerings/Platform]** - Trading features, spot/derivatives/margin, staking, DeFi, specialized products
3. **## Security Measures** - Account security, platform security, historical incidents if any, custodial disclaimers
4. **## User Experience** - Interface, educational resources, customer support, onboarding
5. **## Regulatory Compliance** - Licenses, registrations, challenges, geographic restrictions
6. **## Points to Consider** - 4-5 specific actionable points: fees, risks, complexity, target users
7. **## Conclusion** - Market position, ideal users, balanced verdict sentence summarizing pros/cons
8. **ExchangeButton Component** (MANDATORY) - Add at the very end: `<ExchangeButton href="{website}" text="Join {Exchange Name}" />`

FLEXIBILITY: The 7 sections are MINIMUM. Add contextual sections as needed (e.g., "Founders and Historical Context", "Token Utility", "Proof of Reserves", "Brand Building"). Adapt section 2 header to exchange type.

## Content Requirements

- **Length**: 1,500-2,500 words
- **Internal Links**: 15-20 total, ALL using **[Text](/path)** bold format
- **Images**: Exactly 2 with descriptive alt text using /images/posts/ paths
  - First: After Core Services, before Security
  - Second: After User Experience/Regulatory, before Conclusion
- **Formatting**: ## for main headings, **bold** for ALL sub-categories in bullet points
- **Tone**: Professional, balanced, expert-level, E-E-A-T compliant
- **SEO**: Include naturally 'cryptocurrency exchange', 'crypto trading', 'digital assets'

## Internal Linking (CRITICAL - ALWAYS USE BOLD)

**MANDATORY FORMAT**: **[Text](/path)** NOT [Text](/path)

**Priority Links (MUST include 6+):**

- **[Bitcoin](/posts/what-is-bitcoin)**
- **[Ethereum](/posts/what-is-ethereum)**
- **[DeFi](/posts/what-is-defi)**
- **[Crypto Staking](/posts/crypto-staking)** or **[Proof-of-Stake](/posts/what-is-proof-of-stake)**
- **[How To Store Crypto](/posts/how-to-store-crypto)**
- **[How to Avoid Crypto Scams](/posts/how-to-avoid-crypto-scams)**

**Link Validation Rules**:

- ONLY use links from the provided database (crypto_ogs, posts, exchanges, tools)
- Database format: `key|slug|title`
- Search database for relevant entries (e.g., "bitcoin", "ethereum", "defi", "staking", "nft")
- Check variations: "nft" vs "non-fungible tokens", "crypto scams" vs "scams", "store crypto" vs "storage"
- **Founders**: **[Name](/crypto-ogs/{slug})** - ONLY if name exists in crypto_ogs database
- **Exchanges**: **[Exchange](/exchanges/{slug})** - Use for comparisons (check exchanges database)
- **Concepts**: **[Title](/posts/{slug})** - Use exact slug from posts database
- **Tools**: **[Tool](/tools/{slug})** - Use exact slug from tools database

**Distribute links** evenly across ALL sections, not clustered.

## Writing Standards

- **Specific Numbers**: "200+ cryptocurrencies", "700+ trading pairs", "95%+ cold storage" (NOT "many" or "most")
- **Historical Context**: Include founding year, major incidents with dates, regulatory milestones
- **Risk Warnings**: MUST include for derivatives, custodial risks, regulatory uncertainties
- **Balanced Tone**: Acknowledge strengths AND limitations objectively
- **Actionable Advice**: "Points to Consider" must be specific and useful
- **Natural Voice**: Avoid AI-like filler, vary sentence length, use occasional short sentences

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

## Risk Warning Templates

Include in appropriate sections:

- **Derivatives**: "Trading derivatives, especially with high leverage, carries extreme risk and can result in the loss of your entire position rapidly."
- **Custodial**: "Assets held on [exchange] are under [exchange]'s custody; assess counterparty risk and consider self-custody for long-term storage."
- **Regulatory**: "Users must verify the legality and availability of [exchange] in their country..."
- **Impermanent Loss** (for DEX): "Providing liquidity involves significant risk, including impermanent loss..."

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

- Minimum 8 social platforms (research official accounts only)
- Description: 150-160 characters, SPECIFIC with unique differentiator (NOT generic)
- Required social: website, twitter, app stores (apple/android)

**Description Quality:**
❌ BAD: "comprehensive cryptocurrency trading services with advanced features"  
✅ GOOD: "Leading US-based crypto exchange offering secure trading, staking and educational resources"  
✅ GOOD: "Korea's largest crypto exchange in terms of trading volume and customers"

## Quality Checklist

Before finalizing:

**Structure**

- [ ] Opening: ## **[Exchange Name]: [Specific Descriptor]** (NOT "Brief Description")
- [ ] All 7 core sections present with ## headers
- [ ] Section 2 header adapted to exchange type
- [ ] Conclusion ends with verdict sentence

**Links (CRITICAL)**

- [ ] 15-20 internal links distributed across ALL sections
- [ ] ALL links use **[Text](/path)** bold format
- [ ] Includes 6+ priority links (Bitcoin, Ethereum, DeFi, Staking, Store Crypto, Avoid Scams)
- [ ] Verified all links exist in database (used exact keys)
- [ ] NO guessed URLs or broken links

**Images**

- [ ] Exactly 2 images with descriptive alt text
- [ ] Paths use /images/posts/ (NOT /images/exchanges/)
- [ ] First: After Core Services, before Security
- [ ] Second: After User Experience/Regulatory, before Conclusion

**Content**

- [ ] 1,200+ words minimum
- [ ] Specific numbers throughout (e.g., "200+ cryptocurrencies")
- [ ] Risk warnings for derivatives/custody/regulatory
- [ ] **Bold** formatting for ALL sub-categories
- [ ] Balanced tone (strengths AND limitations)
- [ ] ExchangeButton at the very end
- [ ] Description is specific and unique (not generic)
