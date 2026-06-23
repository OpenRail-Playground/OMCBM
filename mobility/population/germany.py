from __future__ import annotations

import numpy as np
import pandas as pd

from mobility.runtime.assets.file_asset import FileAsset
from mobility.runtime.io.download_file import download_file
from mobility.spatial.admin_units import GermanAdminUnits


class GermanCityLegalPopulation(FileAsset):
    """German legal population by local admin unit."""

    def create_and_get_asset(self) -> pd.DataFrame:
        folder = "data/germany"

        pop = pd.read_csv(
            folder / "legal_population_germany.csv",
            sep=";",
            usecols=["COM", "PTOT"],
            dtype={"COM": str, "PTOT": np.int32},
        )
        pop.columns = ["local_admin_unit_id", "legal_population"]
        pop["local_admin_unit_id"] = "de-" + pop["local_admin_unit_id"]
        pop.to_parquet(self.cache_path)
        return pop


class GermanPopulationGroups:
    """German population groups used to sample individuals."""

    def build(
        self,
        transport_zones,
    ) -> pd.DataFrame:
        folder = "data/germany"
        pop = pd.read_csv(
            folder / "synthetic_population.csv",
            sep=";",
            usecols=["COM", "age", "socio_pro_category"],
            dtype={"COM": str, "age": np.int32, "socio_pro_category": np.int32},
        )
        
        n = len(pop)
        rand = np.random.default_rng(seed=42)

        pop_groups = pd.DataFrame({
            "transport_zone_id": transport_zones[transport_zones["country"] == "de"],
            "local_admin_unit_id": "de-" + pop["COM"],
            "age": pop["age"],
            "socio_pro_category": pop["socio_pro_category"],
            "ref_pers_socio_pro_category": pop["socio_pro_category"],
            "n_pers_household": rand.integers(1, 5, size=n),  # 1 à 4
            "n_cars": rand.integers(0, 2, size=n),            # 0 ou 1
            "weight": 1.0,
            "country": "de",
        })

        return pop_groups
