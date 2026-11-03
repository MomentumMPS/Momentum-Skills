# Story point estimation

Use the current team's estimation method when supplied. Otherwise propose the formula and scale below, make the assumption explicit, and resolve acceptance before writing points. Do not treat this example as a prior approval from the current user. For this method, calculate an estimate and assign a positive Fibonacci value:

```text
net_effort = (human_artificial_intelligence_orchestration_needed_time
              + human_review_time
              + human_manual_operations_required_time)
             - (artificial_intelligence_capacity
                - artificial_intelligence_analysis_time)
```

Use equivalent person-hours for every input so the subtraction is meaningful:

- **Orchestration:** gross human-equivalent time needed to plan, prompt, coordinate, and integrate the work before the AI offset.
- **Review:** human time needed to inspect and validate the outcome.
- **Manual operations:** human work that must be performed manually, including required environment, deployment, or Jira operations.
- **AI capacity:** estimated human-equivalent hours saved by AI assistance for this ticket; not a model benchmark, token budget, or abstract score.
- **AI analysis:** time cost of the AI's analysis, expressed on the same basis. Keep this separate from the other inputs to avoid double counting.

Estimate inputs from ticket scope, dependencies, uncertainty, and verification effort. Record the five inputs, result, selected points, and a short rationale in the pre-creation summary; do not add another section to the required ticket template. A negative result does not mean negative work: retain the calculated result for transparency and assign the minimum of 1 point.

## Conversion to Fibonacci

This suggested starting scale assumes an eight-hour working day; values above 8 extend the same Fibonacci progression. Use a replacement supplied by the current user or team:

| Net equivalent effort | Points |
| --- | --- |
| Up to 4 hours, including zero/negative results | 1 |
| Over 4 through 8 hours | 2 |
| Over 8 through 16 hours | 3 |
| Over 16 through 24 hours | 5 |
| Over 24 through 40 hours | 8 |
| Over 40 through 64 hours | 13 |
| Over 64 through 104 hours | 21 |

For still larger work, explain the uncertainty and recommend splitting; do not create extra tickets without authorization. Extend the sequence only if keeping one ticket is deliberate: each subsequent Fibonacci value has an upper effort bound of eight hours times the preceding Fibonacci value (34 points up to 168 hours, 55 up to 272 hours, and so on). Eight points is unusual but valid and signals several days of work. Do not cap at 5 or assign 8 casually. Treat hours as an estimation aid, not a guarantee of calendar duration.
