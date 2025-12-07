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

- **Specific Numbers & Data**: Use exact numbers "200+ cryptocurrencies", "99.9% reduction", "2,700-4,000 TPS" - AVOID vague terms like "many", "most", "several"
- **Historical Context**: Include founding years, launch dates, key events with dates
- **Risk Context**: Include naturally when discussing features (e.g., "While leverage can amplify profits, it also increases potential losses")
- **Balanced Tone**: Acknowledge strengths AND weaknesses objectively
- **Actionable Content**: Provide practical advice with context, explain "why" not just "what"
- **Natural Voice**: Vary sentence length, avoid AI-like filler ("In conclusion", "Furthermore" - use sparingly), write conversationally but professionally
- **Beginner-Friendly**: Explain technical terms on first use when concept is central, link to foundational content when appropriate. Make complex topics accessible without dumbing down.
- **Concrete Examples**: Include 2 short real-world scenarios or anonymized mini case studies (especially for security, scams, "how to", and risk topics)
- **Directly address reader**: Use "you"/"your" to acknowledge their concerns and goals
- **Use analogies**: Explain complex ideas with simple comparisons
- **Encouraging tone**: Combine honest risk discussion with reassurance, especially for beginners and security topics

## Category Selection (MANDATORY - Use ONLY These Categories)

Choose 1-4 categories from this EXACT list: **Investing**, **Beginners**, **Regulation**, **Bitcoin**, **Adoption**, **Blockchain**, **Technology**, **Web3**, **Predictions**, **Security**, **Politics**, **Sustainability**, **Gaming**, **Nfts**, **Ai**

**Guidelines**: Choose 2-3 optimal categories, match to post's primary focus (not just mentioned terms), quality over quantity.

## Tag Generation

Generate 8-15 SEO-focused tags covering: Primary topic/asset, Technology/concept, Action/use case, Audience, Related topics

## Opening Style

**Requirements:**

- Start with **2–3 short paragraphs**, not a bullet list
- Use at least one: relatable scenario, question hook, or historical context
- Explicitly acknowledge reader's situation and concerns
- Clearly state what they will learn and why it matters now
- Include ONE natural internal link where it adds context

## Conclusion Style

- Every post MUST end with **Conclusion section** using heading `## Conclusion: [Short Benefit-Oriented Phrase]` or `## Conclusion`
- **2–3 paragraphs** (not bullet checklist)
- Summarize key takeaways in plain language, restate why topic matters
- Reinforce confidence that reader can act safely/make better decisions
- Suggest 1–2 practical next steps with natural internal links

## Frontmatter Requirements

**Title Formats:** "What is [Topic]?", "How to [Action]", "Understanding [Topic]", "[Topic]: [Subtitle]", or question format

**Description (CRITICAL - EXACTLY 150-160 characters):**

- VERY SPECIFIC with unique differentiators (NOT generic)
- Formula: [Topic name] + [Key features] + [What readers learn] + [Audience optional]
- ❌ BAD: "Learn about cryptocurrency and how it works"
- ✅ GOOD: "Bitcoin is the world's first cryptocurrency. Learn about its history, how it works, and why it's considered digital gold. Perfect for beginners looking to understand the foundation of the crypto world."

**Image**: `/images/posts/{descriptive-name}.jpg` or `.png`

**Categories**: Array of 1-4 from allowed list

**Tags**: Array of 8-15 relevant keywords

**Crypto OGs (Optional)**: Only when founder/creator mentioned - **MANDATORY: Always capitalize**

- ✅ CORRECT: `crypto-ogs: ["Satoshi Nakamoto", "Vitalik Buterin"]`
- ❌ WRONG: `crypto-ogs: ["satoshi nakamoto", "vitalik buterin"]`

**Exchanges (Optional)**: Only when recommending services - **MANDATORY: Always capitalize**

- ✅ CORRECT: `exchanges: ["Coinbase", "Binance", "Kraken"]`
- ❌ WRONG: `exchanges: ["coinbase", "binance", "kraken"]`

**IMPORTANT - Capitalization (MANDATORY):**

- ALWAYS use proper capitalization for crypto-ogs and exchanges in BOTH frontmatter and content
- ❌ NEVER lowercase: "satoshi nakamoto", "coinbase"
- ✅ ALWAYS proper case: "Satoshi Nakamoto", "Coinbase"

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
  "tags": [
    "bitcoin",
    "cryptocurrency",
    "blockchain",
    "digital gold",
    "crypto investing",
    "crypto basics"
  ],
  "description": "Bitcoin is the world's first cryptocurrency. Learn about its history, how it works, and why it's considered digital gold. Perfect for beginners looking to understand the foundation of the crypto world.",
  "categories": ["Beginners", "Technology", "Blockchain", "Bitcoin"],
  "crypto_ogs": ["Satoshi Nakamoto"],
  "exchanges": ["Coinbase", "Binance", "Kraken"]
}
```

**Requirements:**

- **Tags**: 8-15 SEO-focused keywords
- **Description**: EXACTLY 150-160 characters, SPECIFIC with unique differentiator
- **Categories**: 1-4 from allowed list
- **Crypto OGs/Exchanges**: Optional, only when contextually relevant, ALWAYS capitalized

## Quality Checklist

**Structure**: Engaging opening (2-3 paragraphs), all core sections with ## headers, conclusion (2-3 paragraphs), 1,200-2,500 words

**ArticleAd Placement**: 2-6 ads evenly distributed, after complete sections only, avoid image proximity, first after introduction, last before conclusion

**Links & Images**: 8-15 internal links using **[Text](/path)** bold format, exactly 2 images with descriptive alt text, paths use `/images/posts/`

**Content**: Specific numbers/data, historical context with dates, balanced tone, **bold** formatting for sub-categories, prose paragraphs preferred, no repetitive explanations, technical terms explained naturally, narrative flow
