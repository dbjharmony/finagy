## FinAgy TODO Workflow

The following diagram shows the planned workflow with checkpoints after each major step.

```mermaid
flowchart TD
  A[2025-11-24] --> B[Checkpoint:<br>Stop, evaluate & wait]
  B -->|Continue| C[Design provider abstraction]
  C --> D[Checkpoint:<br>Stop, evaluate & wait]
  D -->|Continue| E[Implement Anthropic adapter]
  E --> F[Checkpoint:<br>Stop, evaluate & wait]
  F -->|Continue| G[Run tests / smoke run]
  G --> H[Checkpoint:<br>Stop, evaluate & wait]
  H -->|Continue| I[Document changes]
  I --> J[Checkpoint:<br>Stop, evaluate & wait]
  J -->|Continue| K[Final:<br>Stop and wait]
```

You can preview by paste the Mermaid block into https://mermaid.live to render it.
