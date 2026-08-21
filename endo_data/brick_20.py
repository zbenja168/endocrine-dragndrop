BRICK = {
    "brick_num": 20,
    "brick_title": "Adrenal Insufficiency, Cushing Syndrome, and Cushing Disease: Localizing HPA Axis Dysfunction",
    "games": [
        {
            "slug": "ai_localization",
            "title": "Where Is the Cortisol Deficiency?",
            "subtitle": "Sort each feature under the level of HPA-axis failure it points to",
            "categories": ["Level of the defect", "Plasma ACTH", "Aldosterone and renin", "Serum potassium", "Skin findings", "Usual cause"],
            "data": {
                "Primary (Addison disease)": {
                    "Level of the defect": "Adrenal cortex itself is destroyed or damaged",
                    "Plasma ACTH": "Elevated, because cortisol negative feedback is lost",
                    "Aldosterone and renin": "Aldosterone often deficient with elevated plasma renin",
                    "Serum potassium": "Hyperkalemia is a strong clue to this level",
                    "Skin findings": "Darkened palmar creases, scars, and mucous membranes",
                    "Usual cause": "Autoimmune adrenalitis, infection, hemorrhage, metastases, infiltration"
                },
                "Secondary or tertiary (central)": {
                    "Level of the defect": "Pituitary or hypothalamus fails to drive the cortex",
                    "Plasma ACTH": "Low or inappropriately normal from pituitary or hypothalamic disease",
                    "Aldosterone and renin": "Preserved; RAAS and potassium still drive the zona glomerulosa",
                    "Serum potassium": "Severe hyperkalemia is unlikely at this level",
                    "Skin findings": "No hyperpigmentation, because ACTH drive is reduced",
                    "Usual cause": "Pituitary or hypothalamic disease reducing ACTH or CRH output"
                },
                "Glucocorticoid-induced": {
                    "Level of the defect": "Prescribed steroid feedback shuts off CRH and ACTH",
                    "Plasma ACTH": "Suppressed by chronic exogenous glucocorticoid exposure",
                    "Aldosterone and renin": "Preserved, since the cortex is intact but under-stimulated",
                    "Serum potassium": "Cortisol deficiency without much rise in potassium",
                    "Skin findings": "No hyperpigmentation; features may instead look cushingoid",
                    "Usual cause": "Abrupt discontinuation of prolonged glucocorticoid therapy"
                }
            }
        },
        {
            "slug": "hpa_testing",
            "title": "Testing the HPA Axis",
            "subtitle": "Match each test to what it measures, the abnormal result, and how it is used",
            "categories": ["What it measures", "Abnormal result", "How it is used"],
            "data": {
                "Morning serum cortisol": {
                    "What it measures": "Cortisol at the peak of the normal circadian rhythm",
                    "Abnormal result": "A low morning value supports cortisol deficiency",
                    "How it is used": "Early screen when adrenal insufficiency is suspected"
                },
                "Plasma ACTH": {
                    "What it measures": "Pituitary corticotroph output reaching the adrenal cortex",
                    "Abnormal result": "Elevated with low cortisol points to adrenal cortex failure",
                    "How it is used": "Localizes the defect; not a screen for Cushing syndrome"
                },
                "Cosyntropin stimulation test": {
                    "What it measures": "Adrenal reserve after synthetic ACTH is given",
                    "Abnormal result": "A blunted cortisol rise supports inadequate adrenal reserve",
                    "How it is used": "May still be normal in recent-onset central adrenal insufficiency"
                },
                "Plasma renin and aldosterone": {
                    "What it measures": "The mineralocorticoid limb of the adrenal cortex",
                    "Abnormal result": "Low aldosterone with high renin indicates mineralocorticoid deficiency",
                    "How it is used": "Decides whether fludrocortisone replacement is needed"
                },
                "Late-night salivary cortisol": {
                    "What it measures": "Cortisol at the expected circadian trough",
                    "Abnormal result": "An elevated late-night value shows loss of circadian suppression",
                    "How it is used": "Recommended initial test to confirm hypercortisolism"
                },
                "1-mg overnight dexamethasone suppression test": {
                    "What it measures": "Whether cortisol production is suppressible by feedback",
                    "Abnormal result": "Failure to suppress cortisol supports hypercortisolism",
                    "How it is used": "Confirms cortisol excess but does not identify its source"
                }
            }
        },
        {
            "slug": "cortisol_excess_sources",
            "title": "Localizing Cortisol Excess",
            "subtitle": "Match each source of glucocorticoid excess to its origin, ACTH pattern, and defining clue",
            "categories": ["Origin of the cortisol excess", "Plasma ACTH pattern", "Defining clue or next step"],
            "data": {
                "Exogenous glucocorticoid exposure": {
                    "Origin of the cortisol excess": "Prescribed oral, inhaled, topical, injected, or intra-articular steroid",
                    "Plasma ACTH pattern": "Suppressed, along with endogenous cortisol production",
                    "Defining clue or next step": "Most common cause overall; exclude it by history first"
                },
                "Cushing disease": {
                    "Origin of the cortisol excess": "Pituitary corticotroph adenoma secreting ACTH",
                    "Plasma ACTH pattern": "High or inappropriately normal despite high cortisol",
                    "Defining clue or next step": "Accounts for most ACTH-dependent disease; pituitary-directed imaging"
                },
                "Ectopic ACTH syndrome": {
                    "Origin of the cortisol excess": "Nonpituitary tumor secreting ACTH",
                    "Plasma ACTH pattern": "Markedly elevated, driving severe cortisol excess",
                    "Defining clue or next step": "Hypertension with hypokalemia; petrosal sinus sampling may localize"
                },
                "Adrenal cortisol-producing tumor": {
                    "Origin of the cortisol excess": "Autonomous cortisol output from the adrenal cortex",
                    "Plasma ACTH pattern": "Suppressed by cortisol negative feedback",
                    "Defining clue or next step": "ACTH-independent pattern; remove the causal adrenal tumor"
                },
                "Nelson syndrome": {
                    "Origin of the cortisol excess": "Corticotroph tumor growing after bilateral adrenalectomy",
                    "Plasma ACTH pattern": "Rises markedly once adrenal cortisol feedback is gone",
                    "Defining clue or next step": "Hyperpigmentation with headache and visual field deficits"
                }
            }
        },
        {
            "slug": "management_priorities",
            "title": "Management by Localization and Urgency",
            "subtitle": "Place the first priority, the ongoing plan, and the teaching point for each scenario",
            "categories": ["First priority", "Ongoing management", "Key teaching point"],
            "data": {
                "Adrenal crisis": {
                    "First priority": "Stress-dose intravenous hydrocortisone with fluid resuscitation",
                    "Ongoing management": "Treat the precipitating illness, then complete endocrine testing",
                    "Key teaching point": "Treatment must not wait for confirmatory endocrine results"
                },
                "Chronic primary adrenal insufficiency": {
                    "First priority": "Daily hydrocortisone or an equivalent glucocorticoid regimen",
                    "Ongoing management": "Add fludrocortisone when aldosterone deficiency is confirmed",
                    "Key teaching point": "Follow salt craving, blood pressure, edema, and electrolytes"
                },
                "Glucocorticoid-induced adrenal suppression": {
                    "First priority": "Avoid abrupt withdrawal; taper once the underlying disease is controlled",
                    "Ongoing management": "Consider morning cortisol testing near physiologic replacement doses",
                    "Key teaching point": "The taper exists to give the HPA axis time to recover"
                },
                "Newly suspected endogenous Cushing syndrome": {
                    "First priority": "Confirm hypercortisolism with a recommended screening test",
                    "Ongoing management": "Use plasma ACTH to localize, then remove the causal tumor",
                    "Key teaching point": "Also treat diabetes, hypertension, osteoporosis, and thrombosis risk"
                },
                "Recently cured Cushing syndrome": {
                    "First priority": "Provide temporary glucocorticoid replacement after tumor removal",
                    "Ongoing management": "Monitor until the previously suppressed HPA axis recovers",
                    "Key teaching point": "Withdrawal symptoms appear as tissues adapt to lower cortisol"
                }
            }
        }
    ]
}
