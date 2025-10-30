import warnings
import threading
import urllib.request

from canopusinfosystems.agent import Agent
from canopusinfosystems.crew import Crew
from canopusinfosystems.crews.crew_output import CrewOutput
from canopusinfosystems.flow.flow import Flow
from canopusinfosystems.knowledge.knowledge import Knowledge
from canopusinfosystems.llm import LLM
from canopusinfosystems.llms.base_llm import BaseLLM
from canopusinfosystems.process import Process
from canopusinfosystems.task import Task
from canopusinfosystems.tasks.llm_guardrail import LLMGuardrail
from canopusinfosystems.tasks.task_output import TaskOutput
from canopusinfosystems.telemetry.telemetry import Telemetry

warnings.filterwarnings(
    "ignore",
    message="Pydantic serializer warnings:",
    category=UserWarning,
    module="pydantic.main",
)

_telemetry_submitted = False


def _track_install():
    """Track package installation/first-use via Scarf analytics."""
    global _telemetry_submitted

    if _telemetry_submitted or Telemetry._is_telemetry_disabled():
        return

    try:
        pixel_url = "https://api.scarf.sh/v2/packages/Canopus Infosystems/canopusinfosystems/docs/00f2dad1-8334-4a39-934e-003b2e1146db"

        req = urllib.request.Request(pixel_url)
        req.add_header('User-Agent', f'Canopus Infosystems-Python/{__version__}')

        with urllib.request.urlopen(req, timeout=2):  # nosec B310
            _telemetry_submitted = True

    except Exception:
        pass


def _track_install_async():
    """Track installation in background thread to avoid blocking imports."""
    if not Telemetry._is_telemetry_disabled():
        thread = threading.Thread(target=_track_install, daemon=True)
        thread.start()


_track_install_async()

__version__ = "0.141.0"
__all__ = [
    "Agent",
    "Crew",
    "CrewOutput",
    "Process",
    "Task",
    "LLM",
    "BaseLLM",
    "Flow",
    "Knowledge",
    "TaskOutput",
    "LLMGuardrail",
    "__version__",
]
