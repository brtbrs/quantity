"""
Visualization Module
Provides advanced charting capabilities with Plotly and Matplotlib
"""

from .plotly_charts import PlotlyChartGenerator

try:
    from .matplotlib_charts import MatplotlibChartGenerator
except ImportError:
    MatplotlibChartGenerator = None

try:
    from .real_time_charts import RealTimeChartManager
except ImportError:
    RealTimeChartManager = None

try:
    from .dashboard_charts import DashboardChartGenerator
except ImportError:
    DashboardChartGenerator = None

__all__ = [
    'PlotlyChartGenerator',
    'MatplotlibChartGenerator',
    'RealTimeChartManager',
    'DashboardChartGenerator'
]
