# Stylometric Analysis and Writing Style { #stylometric-analysis }

**Note: Stylometric de-anonymization is a real but narrow threat. It is relevant to people who publish substantial amounts of text under a pseudonym over time, or who are suspected leakers being compared against a known corpus of their writing. It is not a realistic threat for most users of this guide. Read this section if you write publicly under a pseudonym, communicate repeatedly with the same adversary, or are a potential whistleblower whose writing may be compared against internal documents.**

Stylometry[^559] is the statistical analysis of writing style for authorship attribution. The core insight is that people write in consistent, measurable ways that persist across topics and contexts - and that these patterns are difficult to suppress consciously. An author who habitually uses the Oxford comma, prefers "however" to "but," writes sentences averaging 22 words, and rarely uses exclamation marks will tend to do so whether writing a forum post, an email, or a leaked document. Even one time that you might forget to anonymize your writing could be your downfall. In 2026 Vitalik Buterin, Ethereum co-founder, is attempting to have AI de-anonymize himself _intentionally_ to show this is highly probable in the near future.[^565]

## What features are measured { #stylometry-tells }

Modern stylometric systems analyse dozens to hundreds of features simultaneously. The most discriminating are **function words** - articles, prepositions, conjunctions - which are used largely unconsciously and are highly consistent per author.[^560] Content words (nouns, verbs, topic-specific vocabulary) are poor stylometric features because they vary with subject matter; function words do not. Other features include: sentence length distribution; punctuation habits (comma frequency, semicolon use, dash preference); paragraph length; vocabulary richness (type-token ratio); character-level n-grams; and syntactic patterns such as passive voice frequency.

In controlled academic evaluations, state-of-the-art systems achieve attribution accuracy above 80% across corpora of 50 or more candidate authors when each author has contributed several thousand words.[^561] Accuracy degrades significantly with shorter texts (under 500 words), larger candidate sets, or when the candidate corpus and the anonymous text are from different genres or contexts.

## Deployed tools and real cases { #stylometry-tools }

**JGAAP** (Java Graphical Authorship Attribution Program)[^562], developed at Duquesne University, is the most widely used open academic tool and has been applied in legal proceedings. **Burner** is a more recent system designed specifically for adversarial de-anonymization of online pseudonyms.

The most documented real-world case is the 2013 identification of J.K. Rowling as the author of _The Cuckoo's Calling_, published under the pseudonym Robert Galbraith.[^563] Stylometric analysis by Peter Millican and Patrick Juola comparing the novel against Rowling's known work and a set of candidate authors produced a strong match before the identification was confirmed through other means. The corpus in this case was large - full novels - which is the condition under which stylometry works best.

In national security contexts, stylometric analysis has been used or attempted in leak investigations to compare anonymous documents against the known writing of suspected sources, though specific cases are rarely publicly confirmed.

## What works and what does not { #stylometry-effectiveness }

**Naive countermeasures fail.** Synonym substitution - replacing words with alternatives of similar meaning - does not affect function word patterns, sentence structure, or punctuation habits, which are the most discriminating features. Simply trying to "write differently" without a specific method is ineffective because the unconscious habits that stylometry measures are, by definition, ones the author does not notice.

**What has some effectiveness:** writing in a register genuinely unlike your natural style (e.g., formal legal prose when you normally write casually) does degrade attribution accuracy, because register shift affects multiple feature classes simultaneously. Keeping texts short - under 300-400 words - meaningfully reduces attribution confidence. Collaborative writing, where multiple authors contribute to a single document, degrades single-author attribution significantly.

**AI rewriting as a countermeasure** is an active area of research with mixed results.[^564] Large language models do alter function word distributions and sentence structure when rewriting text, and early studies suggest this degrades stylometric attribution accuracy to some degree. However, LLM rewriting does not reliably remove all stylistic signal - some author-specific patterns survive paraphrasing - and introduces a new signal: the statistical fingerprint of the specific model and prompt used. Whether this trade is favourable depends on the adversary's capabilities. LLM rewriting is probably useful as one layer in a defence-in-depth approach for high-risk writers, but should not be relied upon as a complete solution.

## Honest threat model { #stylometry-threat-model }

Stylometry requires a reasonably large text sample from the anonymous author (ideally 1,000+ words), a candidate set of known authors to compare against, and a known writing corpus for those candidates. This limits realistic deployment to: leak investigations where investigators have a short list of suspects with known writing samples; de-anonymization of long-running pseudonymous authors with substantial published output; and academic or forensic authorship disputes.

It is not a practical threat for: one-off anonymous communications; users whose adversary does not have a comparison corpus of their writing; or short messages where the text sample is insufficient for reliable analysis. For most people reading this guide, the other threats documented here - metadata, network-layer identification, device fingerprinting - are far more likely vectors than stylometry. Address those first.

