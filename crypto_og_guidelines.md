# AI Crypto OG Biography Guidelines

## Structure (Flexible 6-8 Core Sections)

**FLEXIBLE STRUCTURE**: Adapt sections based on the person's story. The following are common patterns, but not rigid requirements:

1. **## [Name]: [Engaging Descriptor/Title]** – Start with a compelling, narrative introduction that immediately establishes who they are, their most significant crypto role, and why they matter. Use specific details, founding years, or defining moments. Make it engaging and story-driven.

2. **## Early Life and Background** – Provide meaningful context about their origins, education, or pre-crypto work that connects to their later impact. Keep it relevant and concise.

3. **## Entry into Crypto** – Describe their discovery of crypto/blockchain, early experiences, motivations, or involvement in early communities. Include specific dates and turning points.

4. **## Major Contributions and Projects** – Highlight their biggest achievements, roles, and innovations with specific years, companies, and measurable outcomes. This is often the longest section.

   - Add 1 image strategically within this section
   - Use **bold internal links** to other OGs, posts, or exchanges naturally

5. **## [Contextual Section]** – Add relevant sections based on the person:

   - **Controversies and Criticism** (if applicable)
   - **Philosophy and Vision** (if they have notable views)
   - **Key Developments** (for ongoing projects)
   - **Public Persona** (for high-profile figures)
   - **Technical Contributions** (for developers)

6. **## Legacy and Influence** – Summarize their long-term impact, influence on the industry, and current standing. End with a balanced, concluding sentence.

**IMAGE PLACEMENT**: Place 2 images strategically throughout the article where they enhance the narrative, not rigidly after specific sections.

---

## Content Requirements

- **Length:** 1,200–2,000 words (longer for more complex figures)
- **Images:** Exactly 2, placed strategically to enhance narrative flow
- **Internal Links:** 8–15 total, using **[Text](/path)** in bold, flowing naturally
- **Tone:** Narrative, engaging, and story-driven — like reading a compelling biography
- **Keywords:** Include terms like "crypto pioneer", "blockchain innovator", "decentralization", "Bitcoin", "Ethereum" naturally
- **Readability:** Vary sentence length, use engaging transitions, avoid dry encyclopedia style

## ArticleAd Placement (MANDATORY)

**Format**: `<ArticleAd />` on its own line with blank lines above and below

**Placement Rules:**

- **After complete sections only** - Place after a full section/subsection concludes, never mid-section
- **Avoid image proximity** - Never place immediately before or after images (maintain at least one complete section between ads and images)
- **Even distribution** - Distribute 2-5 ads evenly throughout (2-3 for shorter bios, 3-5 for longer/complex figures)
- **Natural breaks** - Place at transition points between topics, after opening section, between major sections (Early Life, Entry into Crypto, Major Contributions), before Conclusion (not immediately before)
- **Pattern**: First ad after opening, subsequent ads after major biographical sections, last ad before Conclusion

---

## Internal Linking Rules

**Format:** Always use **bold** — **[Text](/path)**

**Natural Linking Strategy (8-15 total links):**

**DO Link When:**

- **Other crypto OGs**: When naturally mentioning them in context (e.g., "working alongside **[Vitalik Buterin](/crypto-ogs/vitalik-buterin)**")
- **Core concepts in context**: When explaining their work (e.g., "building on **[Ethereum](/posts/what-is-ethereum)**")
- **Exchanges they founded/worked with**: When relevant to their story (e.g., "launched **[Coinbase](/exchanges/coinbase)**")
- **Technologies they developed**: When explaining their contributions
- **Educational content**: When it helps readers understand concepts (e.g., "understanding **[smart contracts](/posts/smart-contracts-and-industries-beyond-crypto)**")

**DON'T Link:**

- Every mention of common terms (blockchain, crypto, trading, etc.)
- With forced phrases like "see our guide on..." or "read more about..."
- Multiple links in the same sentence
- As keyword stuffing or SEO manipulation
- When it interrupts the narrative flow

**Path format:**

- `/crypto-ogs/{slug}` for people
- `/posts/{slug}` for concepts
- `/exchanges/{slug}` for platforms
- `/tools/{slug}` for tools

**GOAL**: Links should feel like natural recommendations that enhance understanding, not mandatory reading assignments.

## Opening Style Examples

**Effective Opening Patterns:**

- **Mystery/Intrigue**: "Satoshi Nakamoto is the universally recognized **pseudonym** for the individual, or group of individuals, who developed the original **[Bitcoin](/posts/what-is-bitcoin)** protocol..."
- **Achievement Focus**: "Vitalik Buterin, a Russian-Canadian programmer and writer born in 1994, is widely recognized as the primary visionary and a key co-founder of **[Ethereum](/posts/what-is-ethereum)**..."
- **Impact Statement**: "Elon Musk, the high-profile entrepreneur leading Tesla, SpaceX, and the social media platform X (formerly Twitter), occupies a unique and often controversial position within the cryptocurrency sphere..."
- **Historical Context**: "Harold 'Hal' Finney (1956–2014) was a highly respected American computer scientist and a pioneering cryptographer, celebrated within the **[Blockchain](/posts/what-is-blockchain)** community as one of the earliest and most crucial contributors to **[Bitcoin](/posts/what-is-bitcoin)**..."

**Avoid**: Generic openings like "John Doe is a crypto entrepreneur who founded..."

## Quote Integration Patterns

**Effective Quote Usage:**

- **Opening Hook**: Use a compelling quote right after the opening paragraph
- **Section Breaks**: Place quotes between major sections to add personality
- **Supporting Evidence**: Use quotes to support claims about their philosophy or vision
- **Historical Context**: Include quotes that capture the era or their mindset

**Quote Format:**

```markdown
> "Quote text here that adds value to the narrative." – Name (Context if needed)
```

**Examples from existing articles:**

- Opening quotes that establish their vision
- Technical quotes that explain their approach
- Philosophical quotes that reveal their thinking
- Historical quotes that capture important moments

---

## Writing Standards

- **Specific Details**: Use exact dates, numbers, and measurable impact (e.g., "founded in 2012", "raised $18 million", "1 million BTC")
- **Balanced Perspective**: Include both achievements and criticisms objectively
- **Narrative Flow**: Vary sentence length, use engaging transitions, create story momentum
- **Factual Accuracy**: Avoid speculation, exaggeration, or unverifiable claims
- **Consistent Voice**: Match the engaging, authoritative tone of existing OG articles
- **Paragraph Structure**: Prefer narrative paragraphs over bullet lists, use bullets only for lists of facts
- **Quote Integration**: Use quotes strategically throughout to add personality and authority
- **Engaging Openings**: Start with compelling details that immediately establish importance

---

## SEO & E‑E‑A‑T

- **Expert Authority**: Demonstrate deep knowledge through specific details and context
- **Factual Foundation**: Include verified historical facts, names, dates, and events
- **Natural Keywords**: Use terms like "crypto pioneer", "blockchain innovator", "decentralization" naturally within the narrative
- **Balanced Coverage**: Mention both contributions and criticisms with proper context
- **Engaging Content**: Write compelling stories that people want to read and share

---

## Final JSON Output (REQUIRED)

After writing the biography, provide a JSON object with verified social links and a short description:

```json
{
  "social": {
    "twitter": "https://twitter.com/username",
    "linkedin": "https://linkedin.com/in/username",
    "wikipedia": "https://en.wikipedia.org/wiki/Name",
    "instagram": "https://instagram.com/username",
    "youtube": "https://youtube.com/@username",
    "github": "https://github.com/username",
    "website": "https://officialsite.com"
  },
  "description": "Founder of Ethereum and one of the most influential figures shaping blockchain innovation and decentralization."
}
```

**Rules:**

- Research and find ACTUAL social media profiles for the person
- Include as many verified social links as possible (Twitter, LinkedIn, Wikipedia, Instagram, YouTube, GitHub, etc.)
- Only include links that actually exist — no guessing or placeholders
- If a platform doesn't exist for the person, don't include it
- Description: 100–150 characters, factual and specific

---

## Quality Checklist

**Structure**

- [ ] Engaging opening that immediately establishes importance
- [ ] Flexible section structure adapted to the person's story
- [ ] 2 images placed strategically to enhance narrative

**Links**

- [ ] 8–15 internal links in bold format
- [ ] Links feel natural and enhance understanding
- [ ] No forced phrases or repetitive linking
- [ ] Links flow with the narrative, not against it

**Content**

- [ ] 1,200–2,000 words (longer for complex figures)
- [ ] Story-driven narrative with engaging flow
- [ ] Specific dates, numbers, and measurable details
- [ ] Balanced coverage of achievements and criticisms
- [ ] Quotes integrated naturally throughout
- [ ] Matches the engaging tone of existing OG pages

**ArticleAd Placement**

- [ ] 2-5 ArticleAd components placed throughout article
- [ ] All ads placed after complete sections (never mid-section)
- [ ] No ads immediately before or after images
- [ ] Ads evenly distributed across article length
- [ ] First ad after opening section, last ad before Conclusion

**JSON**

- [ ] Social + description provided
- [ ] At least 3 valid social links
- [ ] Description 100–150 characters, specific and factual
