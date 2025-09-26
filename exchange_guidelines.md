# Exchange Review Guidelines

## Duplicate Prevention

- **Check content-database.json** before creating any exchange review
- **DO NOT DUPLICATE** any existing exchanges listed in the database
- **Verify uniqueness** by checking both exchange names and slugs

## Content Structure (EXACT ORDER)

1. **Opening Section** (## **[Exchange]: [Specific Descriptor]**): Founding year, founder(s) ONLY if in database, headquarters, key positioning. Must begin with 1–2 positioning sentences that highlight what makes the exchange unique.
2. **Core Services** (## **Core [Platform/Services/Offerings]**): Trading platform, spot/derivatives/margin, staking, DeFi features
3. **Security Measures** (## **Security Measures**): Account security, platform security, historical incidents, custodial disclaimers
4. **User Experience** (## **User Experience**): Interface, educational resources, customer support
5. **Regulatory Compliance** (## **Regulatory Compliance**): Licenses, challenges, geographic restrictions
6. **Points to Consider** (## **Points to Consider**): 4-5 specific points: Fee structures, risks, complexity, target users
7. **Conclusion** (## **Conclusion**): Market position, ideal users, balanced summary. Must end with a mandatory final verdict sentence that sums up pros and cons in one line.
8. **ExchangeButton Component** (MANDATORY): Add ExchangeButton component at the very end of the content with the exchange's website URL and "Join [Exchange Name]" text.

## Content Requirements

- **Length**: 1,500-2,500 words (minimum 1,200)
- **Internal Links**: 15-20 total using content database
- **Images**: Exactly 2 with descriptive alt text (using /images/posts/ paths)
- **Formatting**: Use ## for ALL main headings, **bold** for all sub-categories in bullet points
- **Tone**: Professional, balanced, expert-level, E-E-A-T compliant

## Internal Linking Rules

- **Founders**: [Name](/crypto-ogs/{slug}) - ONLY if founder exists in content database
- **Concepts**: [Title](/posts/{slug})
- **Exchanges**: **[Exchange](/exchanges/{slug})**
- **Tools**: **[Tool](/tools/{slug})**
- **Minimum 15 links**: Enforce this requirement strictly
- **Anchor Text Variety**: Use different anchor text for same target page
- **Contextual Placement**: Links should flow naturally within content
- **Links** should be distributed evenly across all sections, not clustered in one area.

### **CRITICAL: Link Validation Requirements**

- **MANDATORY**: Only use links that exist in the provided databases
- **Key Variations**: Check multiple key variations for same concept:
  - "nft" → check "nfts" in database
  - "altcoin" → check "altcoins" in database
  - "defi" → check "defi" in database
- **No Guessing**: If a link doesn't exist in the database, don't create it
- **Fallback Strategy**: If exact match not found, use related concept from database
- **Validation Process**: Before creating any link, verify it exists in the provided JSON data

### **Common Key Variations to Check**

When looking for links, check these variations in the database:

- **NFTs**: Try "nft" and "nfts" keys
- **Altcoins**: Try "altcoin" and "altcoins" keys
- **DeFi**: Use "defi" key
- **Staking**: Use "staking" key
- **Trading**: Use "crypto trading" key
- **Storage**: Use "store crypto" key
- **Scams**: Use "crypto scams" key

### **Link Format Examples**

✅ **CORRECT** (from database):

- `[Bitcoin](/posts/what-is-bitcoin)`
- `[Ethereum](/posts/what-is-ethereum)`
- `[DeFi](/posts/what-is-defi)`
- `[Staking](/posts/crypto-staking)`
- `[How to Store Crypto](/posts/how-to-store-crypto)`
- `[How to Avoid Crypto Scams](/posts/how-to-avoid-crypto-scams)`

❌ **WRONG** (guessed URLs):

- `[Bitcoin](/posts/bitcoin)`
- `[NFTs](/posts/nfts)`
- `[Altcoins](/posts/altcoins)`
- `[Trading](/posts/trading)`

## Writing Standards

- **Specific Numbers**: Use concrete data (e.g., "200+ cryptocurrencies", "700+ trading pairs")
- **Historical Context**: Include founding story, major incidents, regulatory milestones
- **Risk Warnings**: Always mention custodial risks, regulatory uncertainties, derivatives risks
- **Balanced Tone**: Acknowledge both strengths and limitations objectively
- **Actionable Advice**: "Points to Consider" must be specific and actionable
- **Avoid AI-like filler**: Use a natural editorial voice similar to Binance, Coinbase, and OKX reviews.
- **Vary sentence length**: Include occasional short sentences and rhetorical questions to improve readability.

## Content Patterns & Examples

### **Opening Section Descriptor Examples**

- "A Publicly Traded US-Based Crypto Exchange" (Coinbase)
- "Global Leader in Cryptocurrency Services" (Binance)
- "A Global Hub for Altcoin Trading" (KuCoin)
- "Global Crypto Exchange with Extensive Trading and Web3 Features" (OKX)

### **Section Header Variations**

- **Centralized Exchanges**: "Core Trading Platform", "Core Offerings", "Core Services"
- **DEX/Protocols**: "Core Protocol", "How [Name] Works", "Protocol Features"
- **Multi-Product**: "Core Components", "Ecosystem Services", "Platform Features"

### **Bullet Point Structure**

- **Main Category**: **Bold** with colon (e.g., **- **Trading Platform:\*\*)
- **Sub-categories**: **Bold** with detailed description (e.g., **- **Spot Trading:\*\*)
- **Consistent Format**: ALWAYS use **bold** for ALL sub-categories
- **Descriptive**: Include specific details, numbers, and context

### **Image Requirements**

- **Required**: Exactly **2 images** in content body (not counting frontmatter image)
- **Placement**:
  1. **First image**: After main service descriptions, before security section
  2. **Second image**: After user experience or regulatory section, before conclusion
- **Image Paths**: Use `/images/posts/` for body images, `/images/exchanges/` only for frontmatter
- **Alt Text**: `![Descriptive text about what image shows](/images/posts/relevant-image.png)`

### **Risk Warning Templates**

- **Derivatives**: "Trading derivatives, especially with high leverage, carries extreme risk..."
- **Custodial**: "Assets held on [exchange] are under [exchange]'s custody..."
- **Regulatory**: "Users must verify the legality and availability of [exchange] in their country..."
- **Complexity**: "The platform's complexity may be overwhelming for beginners..."

## Frontmatter Standards

### **Required Fields**

- **title**: Official exchange name (proper capitalization)
- **image**: `/images/exchanges/{exchange-slug}.png`
- **description**: 150-160 characters, highlight key features and unique value proposition
  - **Specificity**: Include unique differentiator, not generic phrases
  - **Keywords**: Must include "cryptocurrency exchange" + key benefit
  - **Examples**:
    - ❌ "comprehensive cryptocurrency trading services"
    - ✅ "US-regulated crypto exchange with institutional custody and GUSD stablecoin"
    - ✅ "Global crypto platform with Visa card, staking, and DeFi wallet"
- **date**: YYYY-MM-DD format (not ISO string)
- **order**: Sequential number from content-database.json
- **authors**: `["Crypto Wiki Team"]`
- **social**: Include website and all available social media links (REQUIRED)
  - Must include: website, twitter, youtube, linkedin, facebook, instagram
  - Optional but recommended: tiktok, telegram, reddit, discord, wikipedia
  - Only include platforms that actually exist for the exchange
- **draft**: `true` for new exchanges

### **Social Media Requirements (ENHANCED)**

- **Minimum 8 social links** required (up from 5)
- **Required platforms**: website, twitter, and iphone / android app store
- **Comprehensive research**: Must research ALL available social media platforms
- **Validation**: AI must research actual social media presence, don't guess URLs
- **Fallback**: If platform doesn't exist for the exchange, don't include it

## Social Media Research Strategy

### **Comprehensive Social Media Discovery**

- **Primary Research**: Check exchange's official website footer, about page, and contact page
- **Secondary Research**: Verify social media presence through official exchange pages
- **App Stores**: Check for official mobile apps (iOS App Store, Google Play Store)
- **Platform Priority**: Research in this order to maximize efficiency

### **Research Order (Resource-Efficient)**

1. **Website Analysis**

   - Check footer links
   - Look for social media icons
   - Check "About Us" or "Contact" pages
   - Look for press kit or media resources

2. **App Store Verification**

   - Search iOS App Store for exchange name
   - Search Google Play Store for exchange name

3. **Social Platform Verification**
   - Check each platform for official account
   - Verify account authenticity
   - Look for official account links on exchange website

### **Social Media Variables (Complete List)**

Use ALL available variables that have actual presence:

```yaml
social:
  website: "https://exchange.com"
  twitter: "https://twitter.com/exchange"
  youtube: "https://youtube.com/@exchange"
  linkedin: "https://linkedin.com/company/exchange"
  facebook: "https://facebook.com/exchange"
  instagram: "https://instagram.com/exchange"
  telegram: "https://t.me/exchange"
  discord: "https://discord.gg/exchange"
  reddit: "https://reddit.com/r/exchange"
  tiktok: "https://tiktok.com/@exchange"
  github: "https://github.com/exchange"
  medium: "https://medium.com/@exchange"
  whatsapp: "https://wa.me/exchange"
  vk: "https://vk.com/exchange"
  wikipedia: "https://en.wikipedia.org/wiki/Exchange"
  apple: "https://apps.apple.com/app/exchange"
  android: "https://play.google.com/store/apps/details?id=com.exchange"
```

### **Validation Rules**

- **Only include platforms with verified presence**
- **Must have official account (not fan pages)**
- **App store links must be official apps**
- **Wikipedia must have dedicated page**
- **Minimum 8 social links required** (up from 5)
- **Must include website, twitter, and at least app stores**

### **Research Checklist**

- [ ] Checked website footer for social links
- [ ] Verified each social platform has official account
- [ ] Confirmed app store presence
- [ ] Validated Wikipedia page exists
- [ ] Ensured minimum 5 social links included
- [ ] Verified all links are working and official

### **Social Media Priority Order**

1. **website** (required)
2. **twitter**
3. **youtube**, **linkedin**, **telegram**
4. **facebook**, **instagram**, **tiktok**
5. **discord**, **reddit**, **github**
6. **wikipedia**

## SEO and Content Optimization

### **Keyword Strategy**

- **Primary Keywords**: Include "cryptocurrency exchange", "crypto trading", "digital assets" naturally
- **Long-tail Keywords**: "best crypto exchange for [specific use case]", "secure cryptocurrency platform"
- **Exchange-specific Keywords**: Include exchange name + key features (e.g., "Binance staking", "Coinbase wallet")
- **Keyword Density**: 1-2% for primary keywords, natural integration throughout content
- **LSI Keywords**: Use related terms like "blockchain", "DeFi", "trading platform", "digital wallet"

### **Meta Optimization**

- **Title Tag**: "[Exchange Name]: [Specific Descriptor] - [Key Benefit]"
- **Meta Description**: 150-160 characters, include primary keyword + call-to-action
- **Header Structure**: Use H2 for main sections, include keywords in headers
- **Image Alt Text**: Include relevant keywords and descriptive text

### **Internal Linking Strategy**

- **Minimum 15 internal links** using provided content database
- **Anchor Text Variety**: Use different anchor text for same target page
- **Contextual Placement**: Links should flow naturally within content
- **Priority Links**: Always include storage and scam prevention links
- **Exchange Comparisons**: Link to other exchanges for context

## ExchangeButton Component Requirements

### **Mandatory Addition**

- **Placement**: Add ExchangeButton component at the very end of the content, after the Conclusion section
- **Format**: Use the exact format shown in examples below
- **URL**: Use the exchange's main website URL from the social media links
- **Text**: Use "Join [Exchange Name]" format (e.g., "Join Coinbase", "Join Binance")

### **ExchangeButton Format**

```jsx
<ExchangeButton
  href="https://exchange-website.com"
  text="Join [Exchange Name]"
/>
```

### **Examples**

- **Coinbase**: `<ExchangeButton href="https://coinbase.com" text="Join Coinbase" />`
- **Binance**: `<ExchangeButton href="https://binance.com" text="Join Binance" />`
- **Gemini**: `<ExchangeButton href="https://gemini.com" text="Join Gemini" />`

### **Requirements**

- **MANDATORY**: Every exchange review must include this component
- **URL Source**: Use the website URL from the social media links in frontmatter
- **Consistent Format**: Always use "Join [Exchange Name]" text format
- **Placement**: Must be the last element in the content, after Conclusion section

## Automation Requirements

- **AI Prompt**: Must request social media links as JSON object
- **Frontmatter Generation**: Must parse and include all social media links from AI response
- **Validation**: Only include platforms that actually exist for the exchange
- **Image Requirements**: Must enforce exactly 2 images in body using /images/posts/ paths
- **Content Structure**: Must follow 7-section format with proper internal linking
- **ExchangeButton**: Must include ExchangeButton component at the end of every exchange review

## AI Prompt Instructions for Social Media Research

### **Social Media Research Instructions**

Before writing the exchange review, conduct comprehensive social media research:

1. **Visit the exchange's official website**
2. **Check the footer and about page for social media links**
3. **Search app stores for official mobile apps**
4. **Verify each social platform has an official account**
5. **Include ALL available social media platforms from this list:**
   - website, twitter, youtube, linkedin, facebook, instagram, telegram, discord, reddit, tiktok, github, medium, whatsapp, vk, wikipedia, apple, android

**Requirements:**

- Minimum 8 social links required
- Only include platforms with verified official presence
- Must include website, twitter, and at least one app store
- Verify all links are working and official
- Include app store links for both iOS and Android if available

### **Research Process (10 minutes total)**

1. **Website Analysis (5 minutes)**

   - Open exchange website
   - Check footer for social media icons
   - Look for "About Us" or "Contact" pages
   - Note all social media links found

2. **App Store Verification (2 minutes)**

   - Search iOS App Store for exchange name
   - Search Google Play Store for exchange name
   - Verify official developer accounts

3. **Social Platform Verification (3 minutes)**
   - Check each platform for official account
   - Verify account authenticity
   - Look for official account links on exchange website

### **Social Media Validation**

Before finalizing the review, verify:

- [ ] All social links are working
- [ ] Accounts are official (not fan pages)
- [ ] App store links are for official apps
- [ ] Minimum 8 social links included
- [ ] Website, twitter, and at least one app store included

## Quality Checklist

### **Content Structure**

- [ ] All 7 sections included in correct order with ## headers
- [ ] Opening header: ## **[Exchange Name]: [Specific Descriptor]** (NOT "Brief Description")
- [ ] All main sections use ## heading format
- [ ] 1,200+ words, professional tone
- [ ] Balanced conclusion with clear user guidance
- [ ] **MANDATORY**: ExchangeButton component added at the end with correct format

### **Internal Linking & SEO**

- [ ] **MANDATORY**: Minimum 15 internal links using content database
- [ ] Founders only linked if they exist in content database
- [ ] Major concepts linked: Staking, NFTs, Blockchain, Trading
- [ ] SEO keywords naturally integrated: 'cryptocurrency exchange', 'crypto trading', 'digital assets'

### **Formatting & Images**

- [ ] Exactly 2 images with descriptive alt text placed within content body (using /images/posts/ paths)
- [ ] First image: After main services, before security
- [ ] Second image: After user experience/regulatory, before conclusion
- [ ] Bullet points use consistent **bold** formatting for ALL sub-categories
- [ ] Section headers match exchange type (Trading Platform vs Protocol)

### **Content Quality**

- [ ] Risk warnings for derivatives/custodial risks
- [ ] Specific, actionable "Points to Consider"
- [ ] Regulatory context includes specific details and dates
- [ ] Professional, expert-level tone throughout

### **Frontmatter & Technical**

- [ ] Frontmatter includes: title, image, description, date (YYYY-MM-DD), order, authors, social, draft
- [ ] **MANDATORY**: Minimum 8 social media links included in frontmatter
- [ ] Website included in social section (not separate field)
- [ ] **MANDATORY**: Description is specific and includes unique value proposition (not generic)
- [ ] Meta description 150-160 characters with primary keyword
- [ ] **MANDATORY**: At least one app store link included (apple or android)
- [ ] All social links verified as official accounts
- [ ] NO "Additional resources" section at the end
