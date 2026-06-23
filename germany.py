import dotenv
import mobility

# Data to get and push in /data/germany before running this:
# - "DE_VG250.gpkg" (https://daten.gdz.bkg.bund.de/produkte/vg/vg250_ebenen_0101/aktuell/vg250_01-01.utm32s.gpkg.ebenen.zip)
# - "MiD23_SAE_Regionalisierung-von-MiD-Ergebnissen_Gemeindedaten.xlsx" (https://www.mobilitaet-in-deutschland.de/pdf/MiD23_SAE_Regionalisierung-von-MiD-Ergebnissen_Gemeindedaten.xlsx)
# - "raumgliederungen-referenzen-2024.xlsx" (https://www.bbsr.bund.de/BBSR/DE/forschung/raumbeobachtung/Raumabgrenzungen/downloads/raumgliederungen-referenzen-2024.xlsx?__blob=publicationFile&v=6)

dotenv.load_dotenv()

mobility.set_params(package_data_folder_path="./data", project_data_folder_path="./data")

# de-083155012074 = Müllheim im Markgräflerland
transport_zones = mobility.TransportZones("de-083155012074", radius=10.0)
print(transport_zones.countries)

# # TODO
# survey = mobility.EMPMobilitySurvey()

# # TODO
# # Create a synthetic population of 1000 people for the area.
# population = mobility.Population(transport_zones, sample_size=1000)

# # TODO
# # Simulate trips for this population with car, walk, and bicycle.
# population_trips = mobility.PopulationGroupDayTrips(
#     population=population,
#     modes=[
#         mobility.CarMode(transport_zones),
#         mobility.WalkMode(transport_zones),
#         mobility.BicycleMode(transport_zones),
#     ],
#     activities=[
#         mobility.OtherActivity(population=population),
#     ],
#     surveys=[survey],
#     parameters=mobility.GroupDayTripsParameters(
#         run=mobility.GroupDayTripsRunParameters(n_iterations=1),
#         mode_sequences=mobility.GroupDayTripsModeSequenceParameters(
#             mode_sequence_search_parallel=False,
#         ),
#     ),
# )

# # TODO
# # Run the weekday model.
# weekday_run = population_trips.run("weekday")
# weekday_plan_steps = weekday_run.get()["plan_steps"].collect()

# # TODO
# # Use population_trips.results(...) as the main entry point for indicators.
# weekday_results = population_trips.results("weekday")
# trip_count_by_mode = weekday_results.metrics.trip_count(
#     by_variable="mode",
#     iterations="last",
#     output="table",
# )

# # TODO
# # Plot origin-destination flows between transport zones.
# od_flow_plot = weekday_results.metrics.trip_count(
#     by_zone=["origin_zone", "destination_zone"],
#     iterations="last",
#     output="plot",
# )

# # TODO
# # Get a report of the parameters used by the model.
# parameters_report = weekday_run.parameters_dataframe()
