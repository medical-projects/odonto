from lxml import etree

from .utils import min_digits, max_digits, strbool
from .message import Message

SCHEDULE_QUERY_TRUE = 0
SCHEDULE_QUERY_FALSE = 1
SCHEDULE_QUERY_DELETE = 3


class Patient(Message):
    class Meta:
        schema = {
            # Sex
            #
            # Sex of patient.
            'sex': {
                'type': 'string',
                'allowed': ('M', 'F'),
                'required': True,
            },

            # Date of birth
            #
            # Patient's date of birth.
            'date_of_birth': {
                'type': 'date',
                'required': True,
            },

            # Patient's title
            #
            # (eg. "Mr")
            'title': {
                'type': 'string',
                'minlength': 1,
                'maxlength': 4,
                'required': False,
            },

            # Patient forename
            #
            # First forename.
            'forename': {
                'type': 'string',
                'minlength': 2,
                'maxlength': 20,
                'required': True,
            },

            # Patient surname
            #
            # Surname of patient.
            'surname': {
                'type': 'string',
                'minlength': 2,
                'maxlength': 20,
                'required': True,
            },

            # Previous surname
            #
            'previous_surname': {
                'type': 'string',
                'minlength': 2,
                'maxlength': 20,
                'required': False,
            },

            # NHS number
            #
            # The patient's unique new NHS number.
            'nhs_number': {
                'type': 'string',
                'minlength': 1,
                'maxlength': 17,
                'required': False,
            },

            # NI number
            #
            # The patient's unique National Insurance Number
            'national_insurance_number': {
                'type': 'string',
                'minlength': 1,
                'maxlength': 9,
                'required': False,
            },

            # Address lines
            #
            'address': {
                'type': 'list',
                'schema': {
                    'type': 'string',
                    'minlength': 1,
                    'maxlength': 32,
                },
                'required': True,
                'minlength': 1,
                'maxlength': 5,
            },

            # Post code
            #
            # Patient's post code
            'postcode': {
                'type': 'string',
                'minlength': 1,
                'maxlength': 8,
                'required': False,
            },
        }


class Treatment(Message):
    """
    Repeating treatment type (used in tst and cur segments).
    """

    class Meta:
        schema = {
            # Treatment code
            #
            'code': {
                'type': 'number',
                'min': min_digits(4),
                'max': max_digits(4),
                'required': True,
            },

            # Number of instances
            #
            # The number of times the treatment code occurs in the
            # course of treatment.
            'instance_count': {
                'type': 'number',
                'min': min_digits(0),
                'max': max_digits(2),
                'required': True,
            },

            # Tooth identification code
            #
            'teeth': {
                'type': 'list',
                'schema': {
                    'type': 'string',
                    'regex': '^[1-8][1-9]$',
                    'required': True,
                },
                'required': True,
                'minlength': 0,
                'maxlength': 36,
            },

        }


class BCDS1Message(Message):
    class Meta:
        schema = {
            # Message reference number
            #
            # Sequential number assigned by the practice application that
            # within contract number (9105) uniquely identifies a message.
            'message_reference_number': {
                'type': 'number',
                'min': min_digits(6),
                'max': max_digits(6),
                'required': True,
            },

            # Performer number
            #
            # Performer number issued by NHSDS.  This will be existing personal
            # number if the dentist has already been issued with one.
            'performer_number': {
                'type': 'number',
                'min': min_digits(6),
                'max': max_digits(6),
                'required': True,
            },

            # DPB PIN
            #
            # Personal identification number assigned to a dentist by the NHSDS
            # used to authorise message transmission.
            'dpb_pin': {
                'type': 'number',
                'min': min_digits(6),
                'max': max_digits(6),
                'required': True,
            },

            # Contract number
            #
            # The provider’s unique contract number.
            'contract_number': {
                'type': 'number',
                'min': min_digits(10),
                'max': max_digits(15),
                'required': True,
            },

            # Location
            #
            # Unique code issued by NSHDS to show main location of address.
            'location': {
                'type': 'number',
                'min': min_digits(6),
                'max': max_digits(6),
                'required': True,
            },

            # Rebsubmission count
            #
            # Indicates that a claimhas been resubmitted to NHSDS following
            # amendment by the site. Increment by 1 for each resubmission.
            'resubmission_count': {
                'type': 'number',
                'min': 1,
                'max': 99,
                'default': 1,
                'required': False,
            },

            'patient': {
                'type': 'dict',
                'schema': Patient.Meta.schema,
                'required': True,
            },

            # Dentist / provider declaration
            #
            'provider_declaration': {
                'type': 'number',
                'allowed': (0, 1, 2, 3, 64, 65, 66, 67),
                'required': False,
            },

            # Schedule query
            'schedule_query': {
                'type': 'number',
                'allowed': (
                    SCHEDULE_QUERY_TRUE,
                    SCHEDULE_QUERY_FALSE,
                    SCHEDULE_QUERY_DELETE,
                ),
                'required': False,
            },

            # Date (of acceptance or registration)
            #
            'date_of_acceptance': {
                'type': 'date',
                'required': True,
            },

            # Date of completion
            #
            'date_of_completion': {
                'type': 'date',
                'required': False,
            },

            # Date of examination
            #
            'date_of_examination': {
                'type': 'date',
                'required': False,
            },

            # Types of claims
            #
            'types_of_claims': {
                'type': 'list',
                'schema': {
                    'type': 'dict',
                    'schema': {
                        # Initial registration
                        #
                        'initial_registration': {
                            'type': 'boolean',
                            'required': True,
                        },

                        # Re-registration
                        #
                        'reregistration': {
                            'type': 'boolean',
                            'required': True,
                        },

                        # Patient under care of other dentist
                        #
                        'care_of_other_dentist': {
                            'type': 'boolean',
                            'required': True,
                        },

                        # Occasional treatment only
                        #
                        'occasional_treatment_only': {
                            'type': 'boolean',
                            'required': True,
                        },

                        # Treatment on referral
                        #
                        'treatment_on_referral': {
                            'type': 'boolean',
                            'required': True,
                        },

                        # Part NHS/private
                        #
                        'part_nhs_private': {
                            'type': 'boolean',
                            'required': True,
                        },
                    },
                },
                'default': [],
                'minlength': 0,
            },

            # Treatment arrangements
            #
            'treatment_arrangements': {
                'type': 'dict',
                'schema': {
                    # Transfer to continuing care
                    #
                    'transfer_to_continuing_care': {
                        'type': 'boolean',
                    },

                    # Treatment necessitated by trauma
                    #
                    'treatment_necessitated_by_trauma': {
                        'type': 'boolean',
                    },

                    # Orthodontic radiographs / study casts
                    #
                    'orthodontic_radiographs_or_study_casts': {
                        'type': 'boolean',
                    },

                    # Disability fee
                    #
                    'disability_fee': {
                        'type': 'boolean',
                    },
                },
                'default': {},
                'required': False,
            },

            # Amount of patient charge in pence. (Zero if no charge)
            #
            'patient_charge_pence': {
                'type': 'number',
                'min': 0,
                'required': True,
            },

            # Currency code of patient charge
            #
            'patient_charge_currency': {
                'type': 'string',
                'default': 'GBP',
                'minlength': 3,
                'maxlength': 3,
                'required': True,
            },

            # Exemption and remission information
            #
            'exception_remission': {
                'type': 'dict',
                'schema': {
                    # Exemption and remission code
                    #
                    'code': {
                        'type': 'number',
                        'minlength': min_digits(2),
                        'maxlength': max_digits(2),
                        'required': True,
                    },

                    # Supporting details
                    #
                    'supporting_details': {
                        'type': 'string',
                        'required': False,
                    },
                },
                'required': False,
            },

            # Tooth specific treatments - specifies treatment relating to
            # specific teeth or non-specific teeth completed or proposed.
            #
            'treatments': {
                'type': 'list',
                'schema': {
                    'type': 'dict',
                    'schema': Treatment.Meta.schema,
                },
                'default': [],
                'minlength': 0,
                'maxlength': 30,
                'required': True,
            },

            # Claims under specific regulation - claim for work done under
            # specific provision and not included in "tooth treatment" (TST)
            # segment.
            #
            'treatments_specific': {
                'type': 'list',
                'schema': {
                    'type': 'dict',
                    'schema': Treatment.Meta.schema,
                },
                'default': [],
                'minlength': 0,
                'maxlength': 8,
                'required': True,
            },


            # Dental chart
            #
            'dental_chart': {
                'type': 'list',
                'schema': {
                    'type': 'dict',
                    'schema': {
                        # Tooth identification code
                        #
                        'tooth': {
                            'type': 'string',
                            'regex': '^[1-8][1-9]$',
                            'required': True,
                        },

                        # Annotation code
                        #
                        #   M: Tooth missing
                        #   Z: Tooth missing and space closed
                        #   R: Root present
                        #   E: Tooth to be extracted
                        #   A: Artificial tooth present
                        #   C: Crown present
                        #   BR: Bridge retainer present
                        #   BP: Bridge pontic present
                        #
                        'annotation': {
                            'type': 'string',
                            'allowed': ('M', 'Z', 'R', 'E', 'A', 'C',
                                        'BR', 'BP'),
                            'required': True,
                        },
                    },
                    'required': True,
                },
                'default': [],
                'minlength': 0,
                'maxlength': 32,
                'required': True,
            },
        }

        xsd_schema = 'xml_bcds1.xsd'

    @staticmethod
    def get_root_xml_element(x):
        root = etree.Element('bcds1')

        root.attrib['schvn'] = '1.0'

        root.attrib['clrn'] = str(x['message_reference_number'])
        root.attrib['perf'] = str(x['performer_number'])
        root.attrib['pin'] = str(x['dpb_pin'])
        root.attrib['cno'] = str(x['contract_number'])
        root.attrib['loc'] = str(x['location'])
        root.attrib['resct'] = str(x['resubmission_count'])

        root.attrib['noseg'] = '5'  # calculated

        pat = etree.SubElement(root, 'pat')
        pat.attrib['sex'] = x['patient']['sex']
        pat.attrib['dob'] = x['patient']['date_of_birth'].strftime('%Y%m%d')
        pat.attrib['ptfn'] = x['patient']['forename']
        pat.attrib['ptsur'] = x['patient']['surname']

        for k, v in {
            'nino': 'national_insurance_number',
            'nhsno': 'nhs_number',
            'ptttl': 'title',
            'prvsur': 'previous_surname',
        }.items():
            if v in x['patient']:
                pat.attrib[k] = x['patient'][v]

        adrdet = etree.SubElement(pat, 'adrdet')
        for text in x['patient']['address']:
            adrln = etree.SubElement(adrdet, 'adrln')
            adrln.text = text
        if 'postcode' in x['patient']:
            adrdet.attrib['pc'] = x['patient']['postcode']

        tda = etree.SubElement(root, 'tda')
        for k, v in {
            'dtdec': 'provider_declaration',
            'sqind': 'schedule_query',
        }.items():
            if v in x:
                tda.attrib[k] = str(x[v])

        trtdatgrp = etree.SubElement(tda, 'trtdatgrp')
        for k, v in {
            'datacc': 'date_of_acceptance',
            'datcp': 'date_of_completion',
            'datexm': 'date_of_examination',
        }.items():
            if v in x:
                trtdatgrp.attrib[k] = x[v].strftime('%y%m%d')

        for vals in x['types_of_claims']:
            clty = etree.SubElement(tda, 'clty')
            for k, v in {
                'inireg': 'initial_registration',
                'rereg': 'reregistration',
                'ptothdt': 'care_of_other_dentist',
                'octrt': 'occasional_treatment_only',
                'trtrfl': 'treatment_on_referral',
                'nhspri': 'part_nhs_private',
            }.items():
                clty.attrib[k] = strbool(vals[v])

        trtarr = etree.SubElement(tda, 'trtarr')
        for k, v in {
            'cc18': 'transfer_to_continuing_care',
            'trttra': 'treatment_necessitated_by_trauma',
            'radmod': 'orthodontic_radiographs_or_study_casts',
            'disfee': 'disability_fee',
        }.items():
            trtarr.attrib[k] = \
                strbool(x['treatment_arrangements'].get(v, False))

        chx = etree.SubElement(root, 'chx')
        chx.attrib['ptchg'] = str(x['patient_charge_pence'])
        chx.attrib['curcd'] = x['patient_charge_currency'].lower()

        if 'exception_remission' in x:
            exrmdet = etree.SubElement(chx, 'exrmdet')
            exrmdet.attrib['exrmcd'] = \
                '{:02d}'.format(x['exception_remission']['code'])

            if 'supporting_details' in x['exception_remission']:
                exrmdet.attrib['sdet'] = \
                    x['exception_remission']['supporting_details']

        def create_treatments(name, data):
            if not data:
                return

            elem = etree.SubElement(root, name)

            for treatment in data:
                reptrtty = etree.SubElement(elem, 'reptrtty')
                reptrtty.attrib['trtcd'] = '{:04d}'.format(treatment['code'])
                reptrtty.attrib['noins'] = \
                    '{:02d}'.format(treatment['instance_count'])

                for x in treatment['teeth']:
                    toid = etree.SubElement(reptrtty, 'toid')
                    toid.text = str(x)

        create_treatments('tst', x['treatments'])
        create_treatments('cur', x['treatments_specific'])

        if x['dental_chart']:
            cht = etree.SubElement(root, 'cht')
            for entry in x['dental_chart']:
                todata = etree.SubElement(cht, 'todata')
                todata.attrib['toid'] = entry['tooth']
                todata.attrib['ancd'] = entry['annotation']

        return root
