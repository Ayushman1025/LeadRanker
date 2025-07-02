# AI Readiness Challenge – Caprae Capital

##  Business Problem
SaaSquatchLeads offers scraped contact lists, but lacks lead scoring and prioritization — creating a gap between data and actionable insights for sales teams.

##  Solution
We built `LeadRanker`, a lightweight scoring tool with business rule–based logic and an intuitive UI. It helps users prioritize leads by title seniority, industry relevance, and LinkedIn credibility.

##  Features
- Reads lead data from `scored_leads.csv`
- Applies a scoring engine (0–10)
- Assigns `High`, `Medium`, or `Low` confidence
- UI with filter + export for sales workflows

##  Tech
- `pandas` for data scoring
- `streamlit` for interface

##  Key Value
Enables faster sales decision-making for acquired SaaS firms, consistent with Caprae’s post-acquisition AI enablement strategy.

##  Output Preview

| Name/Title         | Score | Label  |
|--------------------|-------|--------|
| CEO - Ravi Shah    | 8     | High   |
| CTO - Aarav Kapoor | 6     | Medium |

##  Time Taken
Under 5 hours of development time.
