BRICK = {
    "brick_num": 15,
    "brick_title": "Multiple Endocrine Neoplasia Syndromes: MEN1, MEN2A, MEN2B, and MEN4",
    "games": [
        {
            "slug": "men_syndrome_compare",
            "title": "MEN1 vs MEN2A vs MEN2B vs MEN4",
            "subtitle": "Sort each feature under the multiple endocrine neoplasia syndrome it defines",
            "categories": ["MEN1", "MEN2A", "MEN2B", "MEN4"],
            "data": {
                "Causative gene": {
                    "MEN1": "MEN1, which encodes menin",
                    "MEN2A": "RET proto-oncogene, activating pathogenic variant",
                    "MEN2B": "RET, classically the highest-risk M918T variant",
                    "MEN4": "CDKN1B, which encodes p27Kip1"
                },
                "Genetic mechanism": {
                    "MEN1": "Tumor suppressor; tumors arise on losing the remaining allele",
                    "MEN2A": "Gain-of-function receptor tyrosine kinase signaling",
                    "MEN2B": "Activating RET signaling with the earliest, most aggressive MTC",
                    "MEN4": "Tumor suppressor; loss of the p27 cell-cycle brake"
                },
                "Core tumor pattern": {
                    "MEN1": "Parathyroid tumors, pituitary adenomas, pancreatic/duodenal NETs",
                    "MEN2A": "Medullary thyroid carcinoma, pheochromocytoma, primary hyperparathyroidism",
                    "MEN2B": "Medullary thyroid carcinoma, pheochromocytoma, intestinal ganglioneuromatosis",
                    "MEN4": "Parathyroid and pituitary tumors; GEP-NETs reported less often"
                },
                "Clue that should raise suspicion": {
                    "MEN1": "Young patient with multigland hyperparathyroidism and kidney stones",
                    "MEN2A": "Medullary thyroid carcinoma plus episodic adrenergic spells",
                    "MEN2B": "Mucosal neuromas, thickened lips, marfanoid habitus, severe constipation",
                    "MEN4": "MEN1-like phenotype with negative MEN1 genetic testing"
                },
                "Management priority": {
                    "MEN1": "Lifelong parathyroid, pituitary, and pancreatic/duodenal surveillance",
                    "MEN2A": "Screen for pheochromocytoma before thyroid surgery; RET-guided timing",
                    "MEN2B": "Prophylactic thyroidectomy in infancy; test relatives soon after birth",
                    "MEN4": "MEN1-like surveillance guided by CDKN1B testing and phenotype"
                }
            }
        },
        {
            "slug": "biochemical_localization",
            "title": "Localizing MEN-Associated Tumors",
            "subtitle": "Match each MEN-associated tumor to its cell of origin, biochemical clue, and clinical presentation",
            "categories": ["Cell or tissue of origin", "Biochemical clue", "Classic clinical finding"],
            "data": {
                "Parathyroid tumor": {
                    "Cell or tissue of origin": "Parathyroid glands, often multiple glands at once",
                    "Biochemical clue": "Hypercalcemia with an inappropriately elevated PTH",
                    "Classic clinical finding": "Recurrent kidney stones, bone pain, constipation, fatigue"
                },
                "Pituitary adenoma": {
                    "Cell or tissue of origin": "Anterior pituitary, prolactinoma the classic example",
                    "Biochemical clue": "Serum prolactin, paired with pituitary MRI",
                    "Classic clinical finding": "Pituitary mass effects; prolactinoma treated with a dopamine agonist"
                },
                "Gastrinoma": {
                    "Cell or tissue of origin": "Duodenal or pancreatic neuroendocrine cells",
                    "Biochemical clue": "Elevated serum gastrin level",
                    "Classic clinical finding": "Recurrent peptic ulcers with diarrhea (Zollinger-Ellison syndrome)"
                },
                "Insulinoma": {
                    "Cell or tissue of origin": "Pancreatic islet cells",
                    "Biochemical clue": "Fasting insulin level",
                    "Classic clinical finding": "Fasting hypoglycemic episodes from a functional NET"
                },
                "Medullary thyroid carcinoma": {
                    "Cell or tissue of origin": "Thyroid parafollicular C cells",
                    "Biochemical clue": "Calcitonin, with CEA used in monitoring",
                    "Classic clinical finding": "Thyroid nodule or mass that is not iodine-avid"
                },
                "Pheochromocytoma": {
                    "Cell or tissue of origin": "Adrenal medullary chromaffin cells",
                    "Biochemical clue": "Plasma free or 24-hour urinary fractionated metanephrines",
                    "Classic clinical finding": "Episodic headache, sweating, palpitations, paroxysmal hypertension"
                }
            }
        },
        {
            "slug": "presentation_to_workup",
            "title": "From First Tumor to Next Step",
            "subtitle": "For each presentation, place the suspected syndrome, the gene to test, and the next screening step",
            "categories": ["Syndrome suggested", "Gene to test", "Next screening step"],
            "data": {
                "Young adult with multigland primary hyperparathyroidism": {
                    "Syndrome suggested": "MEN1",
                    "Gene to test": "MEN1 (menin)",
                    "Next screening step": "Prolactin with pituitary MRI, plus gastrin and fasting insulin"
                },
                "Adult with medullary thyroid carcinoma and adrenergic spells": {
                    "Syndrome suggested": "MEN2A",
                    "Gene to test": "RET proto-oncogene",
                    "Next screening step": "Metanephrines for pheochromocytoma before any thyroid surgery"
                },
                "Teenager with mucosal neuromas and marfanoid habitus": {
                    "Syndrome suggested": "MEN2B",
                    "Gene to test": "RET, checking for the M918T variant",
                    "Next screening step": "Calcitonin and neck ultrasound, then urgent thyroidectomy planning"
                },
                "Hyperparathyroidism plus pituitary adenoma, MEN1 testing negative": {
                    "Syndrome suggested": "MEN4",
                    "Gene to test": "CDKN1B (p27Kip1)",
                    "Next screening step": "MEN1-like surveillance once a CDKN1B variant is confirmed"
                }
            }
        },
        {
            "slug": "men_tumor_histology",
            "title": "Histology of MEN-Associated Tumors",
            "subtitle": "Match each tumor to its architecture, its immunostain clue, and the grading or behavior point",
            "categories": ["Histologic architecture", "Immunostain clue", "Grading or behavior point"],
            "data": {
                "Pancreatic neuroendocrine tumor in MEN1": {
                    "Histologic architecture": "Organoid, nested, trabecular, islet-like; salt-and-pepper chromatin",
                    "Immunostain clue": "Chromogranin A, synaptophysin, and nuclear INSM1",
                    "Grading or behavior point": "Graded by mitotic count and Ki-67, separate from differentiation"
                },
                "Medullary thyroid carcinoma": {
                    "Histologic architecture": "Solid nests and trabeculae in fibrous stroma containing amyloid",
                    "Immunostain clue": "Calcitonin, chromogranin, and CEA; Congo red apple-green birefringence",
                    "Grading or behavior point": "Malignant C-cell carcinoma tracked by calcitonin and CEA"
                },
                "Pheochromocytoma": {
                    "Histologic architecture": "Zellballen nests of polygonal or spindle cells, delicate fibrovascular stroma",
                    "Immunostain clue": "S-100 highlighting sustentacular cells around each nest",
                    "Grading or behavior point": "Catecholamine release creates perioperative crisis risk"
                },
                "Poorly differentiated neuroendocrine carcinoma": {
                    "Histologic architecture": "Marked pleomorphism, extensive necrosis, small-cell or large-cell morphology",
                    "Immunostain clue": "Markedly elevated Ki-67 proliferation index",
                    "Grading or behavior point": "Aggressive carcinoma, not a typical MEN1-associated well-differentiated NET"
                }
            }
        }
    ]
}
