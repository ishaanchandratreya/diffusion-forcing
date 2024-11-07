from datasets import Maze2dOfflineRLDataset
from algorithms.diffusion_forcing import DiffusionForcingPlanning
from datasets.offline_rl.maze2d import Maze2dOfflineDatasetWithDist
from .exp_base import BaseLightningExperiment


class PlanningExperiment(BaseLightningExperiment):
    """
    A Partially Observed Markov Decision Process experiment
    """

    compatible_algorithms = dict(
        df_planning=DiffusionForcingPlanning,
    )

    compatible_datasets = dict(
        # Planning datasets
        maze2d_umaze=Maze2dOfflineRLDataset,
        maze2d_medium=Maze2dOfflineRLDataset,
        maze2d_large=Maze2dOfflineRLDataset,
        maze2d_custom=Maze2dOfflineRLDataset,
        maze2d_custom_blocked_dist=Maze2dOfflineDatasetWithDist,
    )
