BRICK = {
    "brick_num": 26,
    "brick_title": "Endocrine Messages to the Kidney: Hyperaldosteronism, ADH Disorders, and Diabetes Insipidus",
    "games": [
        {
            "slug": "two_messages_one_kidney",
            "title": "Two Endocrine Messages, One Renal Executor",
            "subtitle": "Match each signaling molecule to where it comes from, what triggers it, and what it does",
            "categories": ["Source", "Main stimulus for release", "Main action"],
            "data": {
                "Renin": {
                    "Source": "Juxtaglomerular cells of the kidney",
                    "Main stimulus for release": "Low renal perfusion, low NaCl at the macula densa, renal sympathetic input",
                    "Main action": "Starts the cascade that generates angiotensin II"
                },
                "Angiotensin II": {
                    "Source": "Generated in the circulation downstream of renin",
                    "Main stimulus for release": "Renin release from juxtaglomerular cells",
                    "Main action": "Constricts blood vessels and stimulates the adrenal zona glomerulosa"
                },
                "Aldosterone": {
                    "Source": "Zona glomerulosa of the adrenal cortex",
                    "Main stimulus for release": "Angiotensin II, and hyperkalemia acting directly on the gland",
                    "Main action": "Raises ENaC and Na+/K+ ATPase activity in late distal nephron and collecting duct"
                },
                "AVP/ADH": {
                    "Source": "Posterior pituitary",
                    "Main stimulus for release": "High plasma osmolality sensed by hypothalamic osmoreceptors",
                    "Main action": "Binds V2 receptors and inserts aquaporin-2 into the apical membrane"
                },
                "Aquaporin-3 and aquaporin-4": {
                    "Source": "Basolateral membrane of collecting duct principal cells",
                    "Main stimulus for release": "Already in place; used once apical aquaporin-2 lets water enter the cell",
                    "Main action": "Return reabsorbed water from the principal cell to the blood"
                }
            }
        },
        {
            "slug": "primary_vs_secondary_aldo",
            "title": "Primary vs Secondary Aldosteronism",
            "subtitle": "Sort each feature into the form of aldosteronism it describes",
            "categories": ["Primary aldosteronism", "Secondary aldosteronism"],
            "data": {
                "Renin level": {
                    "Primary aldosteronism": "Suppressed, because effective circulating volume is sensed as expanded",
                    "Secondary aldosteronism": "High, and it is the driver of the whole picture"
                },
                "Aldosterone level": {
                    "Primary aldosteronism": "Elevated despite the suppressed renin signal",
                    "Secondary aldosteronism": "Elevated in proportion to the upstream renin drive"
                },
                "Why aldosterone is high": {
                    "Primary aldosteronism": "Adrenal secretion is autonomous and no longer under RAAS feedback",
                    "Secondary aldosteronism": "Adrenal gland is responding appropriately to RAAS activation"
                },
                "Representative causes": {
                    "Primary aldosteronism": "Bilateral adrenal hyperplasia or an aldosterone-producing adenoma",
                    "Secondary aldosteronism": "Renal artery stenosis, heart failure, or cirrhosis"
                },
                "Aldosterone-to-renin ratio": {
                    "Primary aldosteronism": "Inappropriately high, which is what makes it a useful screen",
                    "Secondary aldosteronism": "Not the discriminating finding, since both hormones move together"
                },
                "Classic bedside pattern": {
                    "Primary aldosteronism": "Resistant hypertension with hypokalemia and metabolic alkalosis",
                    "Secondary aldosteronism": "Hypertension attributable to an identifiable upstream trigger"
                }
            }
        },
        {
            "slug": "four_water_disorders",
            "title": "Four Ways to Disrupt the Free-Water Message",
            "subtitle": "Place each laboratory or clinical feature under the water-balance disorder it fits",
            "categories": [
                "AVP deficiency (central DI)",
                "AVP resistance (nephrogenic DI)",
                "Primary polydipsia",
                "SIADH / SIAD"
            ],
            "data": {
                "Where the signal fails": {
                    "AVP deficiency (central DI)": "Not enough AVP/ADH is produced or released",
                    "AVP resistance (nephrogenic DI)": "Kidney does not respond normally to AVP/ADH",
                    "Primary polydipsia": "Excess water intake appropriately suppresses AVP/ADH",
                    "SIADH / SIAD": "AVP/ADH effect persists despite low plasma osmolality"
                },
                "Serum sodium and osmolality": {
                    "AVP deficiency (central DI)": "High or high-normal sodium with high serum osmolality",
                    "AVP resistance (nephrogenic DI)": "Same free-water-loss pattern of high sodium and osmolality",
                    "Primary polydipsia": "Low or low-normal sodium and serum osmolality",
                    "SIADH / SIAD": "Hypotonic hyponatremia: low sodium with low serum osmolality"
                },
                "Urine volume": {
                    "AVP deficiency (central DI)": "High, from failure to reabsorb free water",
                    "AVP resistance (nephrogenic DI)": "High, despite adequate circulating AVP/ADH",
                    "Primary polydipsia": "High, matching the excessive water taken in",
                    "SIADH / SIAD": "Low or normal; this is not a polyuria disorder"
                },
                "Urine osmolality": {
                    "AVP deficiency (central DI)": "Low, so urine is dilute while the serum is hyperosmolar",
                    "AVP resistance (nephrogenic DI)": "Low, because aquaporin-2 insertion cannot be driven",
                    "Primary polydipsia": "Low, an appropriate response to excess water intake",
                    "SIADH / SIAD": "Inappropriately concentrated for the degree of hyponatremia"
                },
                "Water-balance testing": {
                    "AVP deficiency (central DI)": "Desmopressin raises urine osmolality because the kidney can respond",
                    "AVP resistance (nephrogenic DI)": "Desmopressin produces little or no rise in urine osmolality",
                    "Primary polydipsia": "Urine may begin to concentrate during water deprivation as endogenous AVP rises",
                    "SIADH / SIAD": "Diagnosed from the sodium and urine pattern, not from desmopressin"
                },
                "Typical causes": {
                    "AVP deficiency (central DI)": "Pituitary or hypothalamic surgery, trauma, tumor, infiltrative disease",
                    "AVP resistance (nephrogenic DI)": "Lithium, hypercalcemia, hypokalemia, CKD, V2 or aquaporin-2 defects",
                    "Primary polydipsia": "Behavioral or compulsive intake of large volumes of water",
                    "SIADH / SIAD": "Pulmonary or CNS disease, small cell lung carcinoma, SSRIs, carbamazepine"
                }
            }
        },
        {
            "slug": "mechanism_based_treatment",
            "title": "Treat the Disrupted Signal or the Renal Response",
            "subtitle": "Match each disorder to its underlying defect, the test that pins it down, and initial management",
            "categories": ["Underlying defect", "Test that pins it down", "Initial management"],
            "data": {
                "Unilateral primary aldosteronism": {
                    "Underlying defect": "One adrenal gland is the autonomous source of aldosterone",
                    "Test that pins it down": "Adrenal venous sampling lateralizing secretion to one gland",
                    "Initial management": "Adrenalectomy to remove the aldosterone source when surgery is appropriate"
                },
                "Bilateral adrenal hyperplasia": {
                    "Underlying defect": "Both adrenal glands oversecrete aldosterone autonomously",
                    "Test that pins it down": "Adrenal venous sampling showing excess from both glands",
                    "Initial management": "Mineralocorticoid receptor blockade to block aldosterone at the kidney"
                },
                "AVP deficiency (central DI)": {
                    "Underlying defect": "Posterior pituitary fails to supply the free-water signal",
                    "Test that pins it down": "Urine osmolality rises after desmopressin is given",
                    "Initial management": "Desmopressin to replace the missing hormonal signal"
                },
                "AVP resistance (nephrogenic DI)": {
                    "Underlying defect": "Collecting duct cannot execute an intact AVP/ADH message",
                    "Test that pins it down": "Little or no rise in urine osmolality after desmopressin",
                    "Initial management": "Target reversible causes such as lithium or hypercalcemia and lower urine volume"
                },
                "Primary polydipsia": {
                    "Underlying defect": "Water intake exceeds need and suppresses AVP/ADH",
                    "Test that pins it down": "Dilute polyuria with low-normal serum sodium and osmolality",
                    "Initial management": "Reduce the excessive water intake driving the picture"
                },
                "SIADH / SIAD": {
                    "Underlying defect": "Antidiuretic effect continues when it should be switched off",
                    "Test that pins it down": "Concentrated urine in the setting of hypotonic hyponatremia",
                    "Initial management": "Reduce free-water retention and treat the underlying trigger"
                }
            }
        }
    ]
}
