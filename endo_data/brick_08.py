BRICK = {
    "brick_num": 8,
    "brick_title": "Hyperpituitarism",
    "games": [
        {
            "slug": "adenoma_subtypes",
            "title": "Pituitary Adenomas by Cell Lineage",
            "subtitle": "Match each adenoma to its cell of origin, the effect of its hormone excess, and its distinguishing mechanism",
            "categories": ["Cell of origin", "Effect of hormone excess", "Distinguishing mechanism or complication"],
            "data": {
                "Prolactin-secreting adenoma": {
                    "Cell of origin": "Lactotroph",
                    "Effect of hormone excess": "Galactorrhea, low libido, irregular or absent menses",
                    "Distinguishing mechanism or complication": "Prolactin suppresses hypothalamic GnRH, so LH and FSH fall"
                },
                "GH-secreting adenoma": {
                    "Cell of origin": "Somatotroph",
                    "Effect of hormone excess": "Acromegaly in adults, gigantism in children",
                    "Distinguishing mechanism or complication": "Obstructive sleep apnea from pharyngeal soft tissue growth"
                },
                "ACTH-secreting adenoma": {
                    "Cell of origin": "Corticotroph",
                    "Effect of hormone excess": "Hypercortisolism, called Cushing disease",
                    "Distinguishing mechanism or complication": "Hyperpigmentation, since MSH shares the ACTH precursor and activates MCR1"
                },
                "TSH-secreting adenoma": {
                    "Cell of origin": "Thyrotroph",
                    "Effect of hormone excess": "Secondary hyperthyroidism with weight loss and palpitations",
                    "Distinguishing mechanism or complication": "Autonomous TSH drives the thyroid to release excess T4 and T3"
                },
                "Gonadotropin-secreting adenoma": {
                    "Cell of origin": "Gonadotroph",
                    "Effect of hormone excess": "Usually no clinical symptoms of hormone excess",
                    "Distinguishing mechanism or complication": "Comes to attention through mass effect rather than endocrine signs"
                }
            }
        },
        {
            "slug": "mass_effects",
            "title": "Mass Effects of an Enlarging Adenoma",
            "subtitle": "Match each compression pattern to the structure involved, the finding it produces, and its clinical significance",
            "categories": ["Structure involved", "Resulting finding", "Clinical significance"],
            "data": {
                "Optic chiasm compression": {
                    "Structure involved": "Crossing visual fibers immediately superior to the sella",
                    "Resulting finding": "Bitemporal hemianopia with loss of peripheral vision",
                    "Clinical significance": "The finding most specific to a pituitary adenoma"
                },
                "Raised intracranial pressure": {
                    "Structure involved": "Intracranial compartment as the sellar mass expands",
                    "Resulting finding": "Headache, nausea, and vomiting",
                    "Clinical significance": "Nonspecific, shared with any expanding intracranial mass"
                },
                "Lateral cavernous extension": {
                    "Structure involved": "Cavernous sinuses that border the sella laterally",
                    "Resulting finding": "Cranial nerve palsies",
                    "Clinical significance": "Marks tumor growth sideways out of the sella"
                },
                "Suprasellar extension into the brain": {
                    "Structure involved": "Base of the brain beyond the sella turcica",
                    "Resulting finding": "Seizures or obstructive hydrocephalus",
                    "Clinical significance": "Indicates a large, aggressively growing macroadenoma"
                },
                "Pituitary apoplexy": {
                    "Structure involved": "Vessels within the neoplasm itself",
                    "Resulting finding": "Abrupt tumor enlargement with loss of consciousness",
                    "Clinical significance": "Neurosurgical emergency that may be rapidly fatal"
                }
            }
        },
        {
            "slug": "diagnostic_workup",
            "title": "Working Up a Suspected Pituitary Adenoma",
            "subtitle": "Match each test to what it examines, what it shows, and how it moves the diagnosis forward",
            "categories": ["What it examines", "Characteristic result", "Diagnostic role"],
            "data": {
                "MRI of the pituitary": {
                    "What it examines": "The sella turcica and adjacent brain by neuroimaging",
                    "Characteristic result": "A sellar mass under 10 mm or over 10 mm across",
                    "Diagnostic role": "Indicated for any patient with acute headaches or visual field deficits"
                },
                "Paired hormone measurement": {
                    "What it examines": "Serum levels drawn from the patient's blood",
                    "Characteristic result": "A pituitary hormone alongside its target hormone, such as TSH with T4",
                    "Diagnostic role": "Establishes whether the adenoma is functioning"
                },
                "Routine histology": {
                    "What it examines": "Resected tumor tissue under light microscopy",
                    "Characteristic result": "Monomorphic polygonal cells arrayed in sheets or cords",
                    "Diagnostic role": "Cellular monomorphism separates adenoma from normal parenchyma"
                },
                "Reticulin stain": {
                    "What it examines": "The connective tissue scaffold supporting the tumor",
                    "Characteristic result": "Loss of the normal reticulin network",
                    "Diagnostic role": "Accounts for the soft, gelatinous texture of the tumor"
                },
                "Immunohistochemistry": {
                    "What it examines": "Antigens within the tumor cells using antibody stains",
                    "Characteristic result": "Hormones plus lineage-specific transcription factors",
                    "Diagnostic role": "Assigns the tumor to a specific pituitary cell subtype"
                }
            }
        },
        {
            "slug": "treatment_options",
            "title": "Treating Hyperpituitarism",
            "subtitle": "Match each therapy to what it is, when it is chosen, and its key caveat",
            "categories": ["What it is", "When it is chosen", "Key caveat"],
            "data": {
                "Cabergoline": {
                    "What it is": "A long-acting dopamine-receptor agonist",
                    "When it is chosen": "First-line therapy for prolactinomas",
                    "Key caveat": "Lowers prolactin, restores gonadal function, and shrinks the tumor"
                },
                "Bromocriptine": {
                    "What it is": "An older dopamine agonist requiring more frequent dosing",
                    "When it is chosen": "An alternative when cabergoline is not used",
                    "Key caveat": "Nausea, vomiting, dizziness, and orthostatic hypotension are common"
                },
                "Octreotide or lanreotide": {
                    "What it is": "Somatostatin analogs given by injection",
                    "When it is chosen": "High GH in a patient who cannot undergo surgery",
                    "Key caveat": "Also used to suppress TSH before resecting a thyrotroph adenoma"
                },
                "Transsphenoidal surgery": {
                    "What it is": "Resection through the nose and the opened sphenoid bone",
                    "When it is chosen": "Most GH-, ACTH-, and TSH-secreting adenomas",
                    "Key caveat": "Vision recovers best when done within a week of symptom onset"
                },
                "Pituitary radiation": {
                    "What it is": "Directed irradiation of the pituitary gland",
                    "When it is chosen": "Patients who fail or cannot receive drugs and surgery",
                    "Key caveat": "Held in reserve rather than used up front"
                }
            }
        }
    ]
}
