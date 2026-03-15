# Claude Autoresearch — Autonomous Goal-directed Iteration

Inspired by Karpathy's autoresearch, this system enables autonomous, constraint-driven iteration for any task type.

## Core Concept

The framework operates on a simple cycle: "Modify → Verify → Keep/Discard → Repeat." As an autonomous agent, you continuously refine work against measurable outcomes without stopping until manually interrupted.

## Activation Triggers

The autoresearch mode engages when users invoke `/autoresearch`, `/ug:autoresearch`, or use language like "work autonomously," "iterate until done," or "keep improving."

## Setup Requirements

Before entering the loop, complete five preparatory steps:

1. Read all relevant files for comprehensive context
2. Define measurable success criteria (tests passing, performance benchmarks, readability scores)
3. Establish scope boundaries for which files are modifiable
4. Create a results log to track iterations
5. Establish a baseline measurement and confirm readiness

## The Autonomous Loop

The system executes continuously:

- **Review** current state and git history
- **Ideate** the next change based on the goal
- **Modify** one focused change to in-scope files
- **Commit** before verification
- **Verify** using mechanical metrics
- **Decide** whether to keep or revert based on results
- **Log** outcomes and repeat indefinitely

## Key Principles

"NEVER STOP — Loop until manually interrupted." The framework enforces atomic changes, automatic rollback for failures, mechanical verification only, and git-based memory of improvements.

Adaptation occurs through domain-specific metrics while preserving universal principles across backend code, frontend UI, ML training, content, and performance optimization contexts.
