import datetime
from odonto.odonto_submissions.serializers import translate_to_bdcs1

from fp17 import treatments


def annotate(bcds1):
    bcds1.patient.surname = "BULWELL"
    bcds1.patient.forename = "LILY"
    bcds1.patient.address = ["18 HIGH STREET"]
    bcds1.patient.sex = 'F'
    bcds1.patient.date_of_birth = datetime.date(1968, 4, 28)

    bcds1.date_of_acceptance = datetime.date(2017, 4, 1)
    bcds1.date_of_completion = datetime.date(2017, 4, 1)

    # Treatments: "Ethnic Origin 1"
    bcds1.treatments = [
        treatments.PRESCRIPTION,
        treatments.ETHNIC_ORIGIN_1_WHITE_BRITISH,
    ]

    return bcds1


def from_model(bcds1, patient, episode):
    demographics = patient.demographics()
    demographics.surname = "BULWELL"
    demographics.first_name = "LILY"
    demographics.house_number_or_name = "18"
    demographics.street = "HIGH STREET"
    demographics.sex = "Female"
    demographics.date_of_birth = datetime.date(1968, 4, 28)
    demographics.ethnicity = "White british"
    demographics.save()

    episode.fp17treatmentcategory_set.update(
        prescription_only=True
    )

    episode.fp17incompletetreatment_set.update(
        date_of_acceptance=datetime.date(2017, 4, 1),
        completion_or_last_visit=datetime.date(2017, 4, 1)
    )
    translate_to_bdcs1(bcds1, episode)