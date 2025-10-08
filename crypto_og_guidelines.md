# AI Crypto OG Biography Guidelines

## Structure (7 Core Sections + OGProfileLinks)

1. **## [Name]: [Descriptor/Title]**  
   Open with a concise, compelling summary — who this person is, their biggest crypto contribution, and what they represent.  
   Mention founding year(s), nationality if relevant, and how they became known in the crypto space.

2. **## Early Life and Background**  
   Give short but informative context — where they grew up, their studies, first exposure to technology or finance, and traits that shaped their later crypto journey.

3. **## Entry into Crypto**  
   Explain when and how they entered the crypto world.  
   What drew them to it — technical curiosity, ideological motives, or business opportunity.  
   Mention early projects, writings, or collaborations.

4. **## Major Contributions and Projects**  
   Focus on the highlights that define their career:  
   - Companies or protocols they founded  
   - Key innovations or moments of influence  
   - Specific milestones with dates  
   - Measurable impact (user base, market cap, adoption, etc.)  
   Use **bold internal links** naturally to connect to related OGs, posts, or exchanges.

5. **## Controversies and Criticism**  
   Cover challenges, lawsuits, bans, or controversies with a neutral, fact-driven tone.  
   Explain the background and how the crypto community perceives those moments.

6. **## Philosophy and Vision**  
   Describe what drives them — decentralization, privacy, financial freedom, mass adoption, or technological progress.  
   Include notable quotes or ideas that reflect their worldview.

7. **## Legacy and Influence**  
   Wrap up with their overall impact on the crypto space.  
   Mention other figures they influenced and what their story represents in crypto’s evolution.  
   End with a strong, balanced sentence that sums up their mark on blockchain history.

8. **OGProfileLinks Component (MANDATORY)**  
   Add at the very end:  
   ```jsx
   <OGProfileLinks website="{website}" name="{Name}" />
   ```

---

## Content Requirements

- **Length**: 1,200–1,800 words  
- **Images**: 2 total  
  - 1 after “Major Contributions and Projects”  
  - 1 after “Philosophy and Vision” or before “Legacy and Influence”  
- **Internal Links**: 8–15 total, all **bold** and natural  
- **Tone**: Engaging, storytelling, factual, and balanced — same voice as existing OGs  
- **SEO keywords**: naturally include “crypto pioneer”, “blockchain innovator”, “Bitcoin”, “Ethereum”, “decentralization”, “founder”, etc.  
- **Consistency**: Avoid generic phrases like “in conclusion”; keep it readable and human.  

---

## Internal Linking (NATURAL FLOW)

**Always use bold:** **[Text](/path)**  

**When to link:**
- To other **crypto-ogs** when comparing or referencing (e.g., “like **[Vitalik Buterin](/crypto-ogs/vitalik-buterin)**, he pushed boundaries of decentralized tech”).  
- To **posts** when referring to a concept (e.g., “helped shape the concept of **[DeFi](/posts/what-is-defi)**”).  
- To **exchanges** when relevant (e.g., “founded **[Binance](/exchanges/binance)**”).  
- To **tools** if they created or inspired specific products.

**When not to link:**
- Every mention of Bitcoin or blockchain  
- Filler phrases like “read more about”  
- Repeated links to the same article  

**Path format:**  
- `/crypto-ogs/{slug}` for people  
- `/posts/{slug}` for concepts  
- `/exchanges/{slug}` for platforms  
- `/tools/{slug}` for tools  

---

## Writing Standards

- **Use specific numbers & years:** “Founded Binance in 2017”, “Bitcoin reached $60,000 in 2021.”  
- **Balanced storytelling:** Achievements + controversies + vision.  
- **Natural flow:** Short and medium sentences alternating; minimal bullet lists.  
- **No speculation or unverifiable rumors.**  
- **Engaging readability:** Write as if narrating an interesting true story, not a Wikipedia entry.  

---

## SEO & E-E-A-T

- Expert, fact-checked tone.  
- Write for readers first — SEO follows naturally.  
- Include full names, key dates, and crypto milestones.  
- Avoid keyword stuffing.  
- Mention real impact: innovations, influence, criticism, or public statements.  

---

## JSON Output (REQUIRED)

At the end, output a separate JSON object:

```json
{
  "social": {
    "website": "https://officialsite.com",
    "twitter": "https://twitter.com/name",
    "linkedin": "https://linkedin.com/in/name",
    "wikipedia": "https://en.wikipedia.org/wiki/Name"
  },
  "description": "Co-founder of Ethereum and one of the most influential voices shaping blockchain and decentralized technology."
}
```

**Rules**
- Minimum 3 verified social links  
- Only official/verified sources — no guesses  
- Description 100–150 characters, concise and specific  

---

## Quality Checklist

**Structure**
- [ ] All 7 sections + OGProfileLinks component  
- [ ] 2 descriptive images placed correctly  

**Links**
- [ ] 8–15 natural bold internal links  
- [ ] All verified slugs  
- [ ] Links flow smoothly  

**Content**
- [ ] 1,200–1,800 words  
- [ ] Balanced tone and factual accuracy  
- [ ] Proper narrative pacing (no filler)  

**JSON**
- [ ] Social + description only  
- [ ] 3+ valid social URLs  
- [ ] Description is unique, under 150 characters  
