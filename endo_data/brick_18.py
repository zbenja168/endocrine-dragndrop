BRICK = {
    "brick_num": 18,
    "brick_title": "Hyperparathyroidism: Primary, Secondary, and Tertiary",
    "games": [
        {
            "slug": "hpt_subtype_compare",
            "title": "Primary vs Secondary vs Tertiary Hyperparathyroidism",
            "subtitle": "Sort each lab value, cause, and treatment under the subtype of hyperparathyroidism it belongs to",
            "categories": ["Primary", "Secondary", "Tertiary"],
            "data": {
                "Serum PTH": {
                    "Primary": "High, driven autonomously by the diseased gland itself",
                    "Secondary": "High, an appropriate response to chronic hypocalcemia",
                    "Tertiary": "High and autonomous after years of overstimulation"
                },
                "Serum calcium": {
                    "Primary": "Elevated; often the first clue on an incidental blood test",
                    "Secondary": "Low to normal despite the markedly elevated PTH",
                    "Tertiary": "Usually elevated, from hyperplasia of all four glands"
                },
                "Serum phosphate": {
                    "Primary": "Decreased, or at the lower limit of the normal range",
                    "Secondary": "Elevated, from low glomerular filtration of phosphate",
                    "Tertiary": "Usually elevated, from renal phosphate retention in ESRD"
                },
                "Calcitriol (1,25-dihydroxy vitamin D)": {
                    "Primary": "Increased, because high PTH stimulates 1-alpha-hydroxylase",
                    "Secondary": "Low, because the diseased kidney stops producing it",
                    "Tertiary": "Usually low, still limited by end-stage kidney disease"
                },
                "Usual underlying cause": {
                    "Primary": "Parathyroid adenoma on one of the four glands",
                    "Secondary": "Chronic kidney disease; also malabsorption or vitamin D deficiency",
                    "Tertiary": "End-stage renal disease treated with long-term dialysis"
                },
                "Preferred management": {
                    "Primary": "Surgical removal of the adenoma; bisphosphonate or cinacalcet if surgery is not an option",
                    "Secondary": "Dietary phosphate restriction, phosphate binders, vitamin D receptor activator",
                    "Tertiary": "Parathyroidectomy; secretion may subside after kidney transplant"
                }
            }
        },
        {
            "slug": "pth_actions",
            "title": "How PTH Raises Calcium and Lowers Phosphate",
            "subtitle": "Match each site of PTH action to what PTH does there and how it moves serum calcium and phosphate",
            "categories": ["What PTH does at this site", "Effect on serum calcium", "Effect on serum phosphate"],
            "data": {
                "Renal tubule, calcium handling": {
                    "What PTH does at this site": "Increases reabsorption of filtered calcium",
                    "Effect on serum calcium": "Rises, because filtered calcium is conserved instead of lost",
                    "Effect on serum phosphate": "Unchanged by this particular transport step"
                },
                "Renal tubule, phosphate handling": {
                    "What PTH does at this site": "Decreases reabsorption of filtered phosphate",
                    "Effect on serum calcium": "Unchanged by this particular transport step",
                    "Effect on serum phosphate": "Falls, because phosphate is dumped into the urine"
                },
                "Bone": {
                    "What PTH does at this site": "Indirectly stimulates osteoclast activity and bone resorption",
                    "Effect on serum calcium": "Rises as mineral is released out of resorbed bone",
                    "Effect on serum phosphate": "Rises, since phosphate leaves bone alongside the calcium"
                },
                "Renal 1-alpha-hydroxylase": {
                    "What PTH does at this site": "Stimulates the enzyme that makes active vitamin D (calcitriol)",
                    "Effect on serum calcium": "Rises indirectly, once calcitriol reaches the gut",
                    "Effect on serum phosphate": "Rises indirectly, once calcitriol reaches the gut"
                },
                "Small intestine": {
                    "What PTH does at this site": "Acts through calcitriol to absorb dietary minerals",
                    "Effect on serum calcium": "Rises from increased intestinal calcium absorption",
                    "Effect on serum phosphate": "Rises from increased intestinal phosphate absorption"
                },
                "Whole-body net result": {
                    "What PTH does at this site": "Coordinates kidney, bone, and vitamin D at once",
                    "Effect on serum calcium": "Net increase; hypercalcemia when PTH is in excess",
                    "Effect on serum phosphate": "Net decrease; hypophosphatemia when PTH is in excess"
                }
            }
        },
        {
            "slug": "bone_and_hypercalcemia_complications",
            "title": "Complications of Chronic PTH Excess",
            "subtitle": "Match each complication to the setting it appears in, its mechanism, and its hallmark finding",
            "categories": ["Setting in which it appears", "Underlying mechanism", "Hallmark finding"],
            "data": {
                "Osteitis fibrosa cystica": {
                    "Setting in which it appears": "Chronic PTH excess, whether primary or secondary",
                    "Underlying mechanism": "Osteoblast RANK-L binds osteoclast RANK, driving bone breakdown",
                    "Hallmark finding": "High-turnover bone disease, also called von Recklinghausen disease of bone"
                },
                "Brown tumor": {
                    "Setting in which it appears": "Long-standing osteitis fibrosa cystica",
                    "Underlying mechanism": "Hemorrhage into a cystic space leaves hemosiderin in fibrous stroma",
                    "Hallmark finding": "Brown cystic bone lesion that is not a true neoplasm"
                },
                "Renal osteodystrophy": {
                    "Setting in which it appears": "Chronic kidney disease and end-stage renal disease",
                    "Underlying mechanism": "High PTH plus acidosis, phosphate retention, and low calcitriol",
                    "Hallmark finding": "Bone and joint pain, deformity, fractures, decreased mobility"
                },
                "Osteomalacia of renal disease": {
                    "Setting in which it appears": "Metabolic acidosis accompanying chronic kidney disease",
                    "Underlying mechanism": "Acidosis dissolves hydroxyapatite and demineralizes bone matrix",
                    "Hallmark finding": "Soft, undermineralized bone that worsens the osteodystrophy"
                },
                "Nephrolithiasis of hypercalcemia": {
                    "Setting in which it appears": "Symptomatic hypercalcemia of primary hyperparathyroidism",
                    "Underlying mechanism": "High serum calcium raises the calcium load filtered into urine",
                    "Hallmark finding": "Flank pain with hematuria, the stones of bones-stones-groans-moans"
                },
                "Hungry bone syndrome": {
                    "Setting in which it appears": "The days immediately following parathyroidectomy",
                    "Underlying mechanism": "Bone rapidly takes up and mineralizes circulating minerals",
                    "Hallmark finding": "Hypocalcemia, hypomagnesemia, hypophosphatemia, and hyperkalemia"
                }
            }
        },
        {
            "slug": "diagnostics_and_therapy",
            "title": "Tests and Treatments for Hyperparathyroidism",
            "subtitle": "Match each test or drug to how it works, when it is used, and its key caveat",
            "categories": ["How it works", "When it is used", "Key caveat or expected result"],
            "data": {
                "Neck ultrasound": {
                    "How it works": "Images the parathyroid glands directly through the soft tissues of the neck",
                    "When it is used": "Sorting out whether one gland or all four are abnormal",
                    "Key caveat or expected result": "Adenoma is oval, well-defined, homogeneous, and hypoechoic in a single gland"
                },
                "Technetium-99 sestamibi scan": {
                    "How it works": "Radiotracer is taken up by mitochondria within parathyroid tissue",
                    "When it is used": "Pinpointing a single overactive gland before an operation",
                    "Key caveat or expected result": "Considerably less accurate when the problem is four-gland hyperplasia"
                },
                "Parathyroidectomy": {
                    "How it works": "Removes the overactive gland or the adenoma outright",
                    "When it is used": "Definitive cure of primary disease and treatment of tertiary disease",
                    "Key caveat or expected result": "Technically difficult; may leave hypoparathyroidism or hungry bone syndrome"
                },
                "Alendronate": {
                    "How it works": "Bisphosphonate that directly inactivates osteoclasts",
                    "When it is used": "Protecting bone density when surgery is deferred or declined",
                    "Key caveat or expected result": "Slows bone loss but leaves the offending adenoma in place"
                },
                "Cinacalcet": {
                    "How it works": "Calcimimetic that binds parathyroid calcium receptors to shut off PTH release",
                    "When it is used": "Severe hypercalcemia before surgery, or long-term if surgery is not possible",
                    "Key caveat or expected result": "Fools the gland into sensing calcium that is not actually there"
                },
                "Sevelamer": {
                    "How it works": "Non-calcium binder that traps dietary phosphate inside the intestinal lumen",
                    "When it is used": "Taken with meals in secondary hyperparathyroidism from chronic kidney disease",
                    "Key caveat or expected result": "Avoids the added calcium load that calcium acetate would impose"
                }
            }
        }
    ]
}
