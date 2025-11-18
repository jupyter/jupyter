"""
Multi-Platform AI Orchestration

Workflow templates for sequential AI platform usage (Perplexity → Claude → GPT).
"""

from typing import Dict, List, Optional, Callable, Any
from dataclasses import dataclass
from enum import Enum
from pathlib import Path


class WorkflowStage(Enum):
    """Sequential stages in multi-platform research workflow."""
    RESEARCH = "research"           # Perplexity: contextual research
    ANALYSIS = "analysis"           # Claude: strategic synthesis
    GENERATION = "generation"       # GPT: creative variations
    REFINEMENT = "refinement"       # Iterative improvement


@dataclass
class WorkflowStep:
    """Single step in multi-platform workflow."""
    stage: WorkflowStage
    platform: str
    prompt_template: str
    expected_output: str
    dependencies: List[str] = None  # Previous step outputs needed

    def __post_init__(self):
        if self.dependencies is None:
            self.dependencies = []


class MultiPlatformOrchestrator:
    """
    Orchestrate sequential AI workflows across platforms.

    Implements the recommended pattern:
    Perplexity (research) → Claude (analysis) → GPT (generation)
    """

    def __init__(self):
        """Initialize orchestrator with workflow templates."""
        self.workflows = {}
        self.results = {}

        # Register default workflows
        self._register_default_workflows()

    def _register_default_workflows(self) -> None:
        """Register common workflow patterns."""

        # Literary Analysis Workflow
        self.register_workflow(
            'literary_analysis',
            steps=[
                WorkflowStep(
                    stage=WorkflowStage.RESEARCH,
                    platform='perplexity',
                    prompt_template=(
                        "Research scholarly perspectives on {topic} in {work}. "
                        "Find recent criticism, historical context, and key debates."
                    ),
                    expected_output='Citations and scholarly context'
                ),
                WorkflowStep(
                    stage=WorkflowStage.ANALYSIS,
                    platform='claude',
                    prompt_template=(
                        "Synthesize research findings:\n{research_output}\n\n"
                        "Analyze patterns, identify frameworks, map conceptual structures."
                    ),
                    expected_output='Strategic synthesis and frameworks',
                    dependencies=['research']
                ),
                WorkflowStep(
                    stage=WorkflowStage.GENERATION,
                    platform='gpt',
                    prompt_template=(
                        "Based on analysis:\n{analysis_output}\n\n"
                        "Generate creative interpretations, alternative readings, "
                        "experimental connections to {comparison_works}."
                    ),
                    expected_output='Creative variations and experiments',
                    dependencies=['analysis']
                )
            ]
        )

        # Atomization Workflow
        self.register_workflow(
            'text_atomization',
            steps=[
                WorkflowStep(
                    stage=WorkflowStage.RESEARCH,
                    platform='perplexity',
                    prompt_template=(
                        "Research computational text analysis methods: n-grams, "
                        "entropy measures, information theory applications to {genre}."
                    ),
                    expected_output='Technical methodology references'
                ),
                WorkflowStep(
                    stage=WorkflowStage.ANALYSIS,
                    platform='claude',
                    prompt_template=(
                        "Given atomization results:\n{atomization_data}\n\n"
                        "And methodology:\n{research_output}\n\n"
                        "Identify significant patterns, interpret entropy shifts, "
                        "map recursive structures."
                    ),
                    expected_output='Pattern interpretation',
                    dependencies=['research']
                ),
                WorkflowStep(
                    stage=WorkflowStage.GENERATION,
                    platform='grok',
                    prompt_template=(
                        "Act as Recursive Data Alchemist. Transform patterns:\n{analysis_output}\n\n"
                        "Generate alternative glyph mappings, experimental visualizations, "
                        "variant compression schemes."
                    ),
                    expected_output='Creative atomization variants',
                    dependencies=['analysis']
                ),
                WorkflowStep(
                    stage=WorkflowStage.REFINEMENT,
                    platform='claude',
                    prompt_template=(
                        "Refine experimental outputs:\n{generation_output}\n\n"
                        "Validate against original data, optimize for clarity, "
                        "document methodology."
                    ),
                    expected_output='Refined analysis',
                    dependencies=['generation']
                )
            ]
        )

    def register_workflow(self, name: str, steps: List[WorkflowStep]) -> None:
        """
        Register a custom workflow.

        Args:
            name: Workflow identifier
            steps: List of workflow steps
        """
        self.workflows[name] = steps

    def get_workflow_template(self, workflow_name: str) -> str:
        """
        Generate markdown template for workflow.

        Args:
            workflow_name: Name of registered workflow

        Returns:
            Formatted markdown template
        """
        if workflow_name not in self.workflows:
            raise ValueError(f"Unknown workflow: {workflow_name}")

        steps = self.workflows[workflow_name]
        lines = [
            f"# Multi-Platform Workflow: {workflow_name.replace('_', ' ').title()}",
            "\nExecute these steps sequentially:\n"
        ]

        for i, step in enumerate(steps, 1):
            lines.append(f"## Step {i}: {step.stage.value.title()} ({step.platform.upper()})")
            lines.append(f"\n**Expected Output:** {step.expected_output}\n")
            lines.append("**Prompt:**")
            lines.append(f"```\n{step.prompt_template}\n```\n")

            if step.dependencies:
                lines.append(f"**Dependencies:** {', '.join(step.dependencies)}\n")

            lines.append("**Output:**")
            lines.append("```\n[Paste {platform} output here]\n```\n")
            lines.append("---\n")

        return '\n'.join(lines)

    def generate_workflow_file(self, workflow_name: str, output_path: Path, params: Optional[Dict] = None) -> Path:
        """
        Generate workflow template file with parameters filled.

        Args:
            workflow_name: Name of registered workflow
            output_path: Path to save workflow file
            params: Optional parameters to fill in template

        Returns:
            Path to generated workflow file
        """
        template = self.get_workflow_template(workflow_name)

        # Fill in parameters if provided
        if params:
            for key, value in params.items():
                template = template.replace(f"{{{key}}}", str(value))

        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(template)

        return output_path

    def validate_workflow_completion(self, workflow_file: Path) -> Dict[str, Any]:
        """
        Check which workflow steps have been completed.

        Args:
            workflow_file: Path to workflow file

        Returns:
            Validation report
        """
        with open(workflow_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Simple check: look for placeholder text in output sections
        placeholder = "[Paste"
        completed_steps = content.count("```") // 2 - content.count(placeholder)
        total_steps = content.count("## Step")

        return {
            'total_steps': total_steps,
            'completed_steps': completed_steps,
            'completion_rate': completed_steps / total_steps if total_steps > 0 else 0,
            'is_complete': completed_steps == total_steps
        }
