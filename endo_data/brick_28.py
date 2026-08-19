BRICK = {
    "brick_num": 28,
    "brick_title": "Adrenal Masses: Incidentaloma, Functional Workup, and Adrenal Tumors",
    "games": [
        {
            "slug": "hormone_phenotypes",
            "title": "Hormone Phenotypes of a Functional Adrenal Mass",
            "subtitle": "Match each hormone excess to the adrenal region that makes it, its clinical clues, and the tumor most associated with it",
            "categories": ["Region of origin", "Clinical clues", "Tumor most associated"],
            "data": {
                "Cortisol excess": {
                    "Region of origin": "Zona fasciculata of the adrenal cortex",
                    "Clinical clues": "Weight gain, proximal weakness, easy bruising, hyperglycemia, osteoporosis",
                    "Tumor most associated": "Cortisol-producing cortical adenoma, or adrenocortical carcinoma"
                },
                "Aldosterone excess": {
                    "Region of origin": "Zona glomerulosa of the adrenal cortex",
                    "Clinical clues": "Hypertension, hypokalemia, metabolic alkalosis, suppressed renin",
                    "Tumor most associated": "Aldosteronoma, or bilateral adrenal hyperplasia"
                },
                "Androgen excess": {
                    "Region of origin": "Zona reticularis of the adrenal cortex",
                    "Clinical clues": "Rapid hirsutism, virilization, acne, menstrual irregularity",
                    "Tumor most associated": "Adrenocortical carcinoma secreting androgens or steroid precursors"
                },
                "Catecholamine excess": {
                    "Region of origin": "Adrenal medulla, which makes epinephrine and norepinephrine",
                    "Clinical clues": "Episodic headache, palpitations, diaphoresis, tremor, pallor",
                    "Tumor most associated": "Pheochromocytoma, or extra-adrenal paraganglioma"
                }
            }
        },
        {
            "slug": "biochemical_workup",
            "title": "Biochemical Workup of an Adrenal Incidentaloma",
            "subtitle": "Match each test to the hormone excess it evaluates, when it is ordered, and the tumor it is looking for",
            "categories": ["Hormone excess evaluated", "Indication in the workup", "Tumor being sought"],
            "data": {
                "1-mg overnight dexamethasone suppression test": {
                    "Hormone excess evaluated": "Autonomous cortisol secretion",
                    "Indication in the workup": "Recommended for essentially every adrenal incidentaloma",
                    "Tumor being sought": "Cortisol-producing adrenal cortical adenoma"
                },
                "Aldosterone, renin, and aldosterone-to-renin ratio": {
                    "Hormone excess evaluated": "Mineralocorticoid excess from primary aldosteronism",
                    "Indication in the workup": "Ordered when hypertension or hypokalemia is present",
                    "Tumor being sought": "Aldosteronoma or bilateral adrenal hyperplasia"
                },
                "Plasma free or urinary fractionated metanephrines": {
                    "Hormone excess evaluated": "Catecholamine excess",
                    "Indication in the workup": "Required before biopsy or surgery, and for indeterminate masses",
                    "Tumor being sought": "Pheochromocytoma or paraganglioma"
                },
                "Serum androgens and steroid precursors": {
                    "Hormone excess evaluated": "Adrenal androgen excess",
                    "Indication in the workup": "Added when virilization or carcinoma is suspected",
                    "Tumor being sought": "Adrenocortical carcinoma"
                }
            }
        },
        {
            "slug": "lesion_imaging_id",
            "title": "Naming the Adrenal Lesion from Its Imaging",
            "subtitle": "Match each adrenal lesion to its characteristic imaging finding, its typical patient or origin, and what it means for management",
            "categories": ["Characteristic imaging finding", "Typical patient or origin", "Management implication"],
            "data": {
                "Lipid-rich cortical adenoma": {
                    "Characteristic imaging finding": "Homogeneous, noncontrast attenuation of 10 HU or less",
                    "Typical patient or origin": "Adult; the most common adrenal incidentaloma",
                    "Management implication": "Benign imaging phenotype; no additional imaging usually required"
                },
                "Adrenal myelolipoma": {
                    "Characteristic imaging finding": "Macroscopic fat with negative attenuation values",
                    "Typical patient or origin": "Adult; mature adipose tissue plus hematopoietic elements",
                    "Management implication": "Usually nonfunctional; review if growth or hemorrhage appears"
                },
                "Adrenocortical carcinoma": {
                    "Characteristic imaging finding": "Large, heterogeneous, necrotic, calcified, with irregular margins",
                    "Typical patient or origin": "Adult cortical tumor that is often hormonally functional",
                    "Management implication": "Prompt endocrine and surgical evaluation, not casual surveillance"
                },
                "Pheochromocytoma": {
                    "Characteristic imaging finding": "Chameleon: heterogeneous, avidly enhancing, cystic, or T2-bright",
                    "Typical patient or origin": "Adult adrenal medulla or extra-adrenal sympathetic tissue",
                    "Management implication": "Exclude biochemically before any biopsy or manipulation"
                },
                "Adrenal neuroblastoma": {
                    "Characteristic imaging finding": "Calcified heterogeneous mass crossing midline and encasing vessels",
                    "Typical patient or origin": "Young child; adrenal medulla or sympathetic chain",
                    "Management implication": "Pediatric oncologic evaluation of the adrenal-region mass"
                },
                "Benign adrenal cyst": {
                    "Characteristic imaging finding": "Thin-walled, fluid-filled, simple cystic signal on MRI",
                    "Typical patient or origin": "Adult; a nonneoplastic fluid collection, not a tumor",
                    "Management implication": "Reassuring unless thick walls or mural nodules develop"
                }
            }
        },
        {
            "slug": "three_triage_questions",
            "title": "The Three Questions Every Adrenal Mass Must Answer",
            "subtitle": "Sort each row into the triage question it belongs to",
            "categories": ["Is the mass functional?", "Is the mass malignant?", "Is the mass dangerous to touch?"],
            "data": {
                "What the question asks": {
                    "Is the mass functional?": "Does this lesion secrete a clinically important hormone excess?",
                    "Is the mass malignant?": "Do the imaging features look benign, indeterminate, or suspicious?",
                    "Is the mass dangerous to touch?": "Could manipulating it trigger a catecholamine surge?"
                },
                "How it is answered": {
                    "Is the mass functional?": "Biochemical testing of cortisol, aldosterone, and catecholamine axes",
                    "Is the mass malignant?": "Noncontrast CT attenuation, homogeneity, size, margins, interval growth",
                    "Is the mass dangerous to touch?": "Plasma free or 24-hour urinary fractionated metanephrines"
                },
                "Finding that raises concern": {
                    "Is the mass functional?": "Hypokalemic hypertension, easy bruising, or rapid virilization",
                    "Is the mass malignant?": "Larger than 4 cm, heterogeneous, necrotic, invasive, or growing",
                    "Is the mass dangerous to touch?": "Episodic headache, palpitations, sweating, tremor, and pallor"
                },
                "Rule to remember": {
                    "Is the mass functional?": "Assume potentially functional until the workup says otherwise",
                    "Is the mass malignant?": "Imaging characterizes the mass but never proves function",
                    "Is the mass dangerous to touch?": "Do not biopsy until pheochromocytoma has been excluded"
                }
            }
        }
    ]
}
