BRICK = {
    "brick_num": 32,
    "brick_title": "Obesity and Metabolic Syndrome",
    "games": [
        {
            "slug": "hunger_hormones",
            "title": "Hunger and Satiety Hormones",
            "subtitle": "Match each hormone to its source, effect on food intake, and distinctive feature",
            "categories": ["Source", "Effect on food intake", "Distinctive feature"],
            "data": {
                "Ghrelin": {
                    "Source": "Gastric secretions from the fundus of the stomach",
                    "Effect on food intake": "Increases food intake and decreases energy expenditure",
                    "Distinctive feature": "Rises before meals; lower in obesity but rises again with weight loss"
                },
                "Leptin": {
                    "Source": "Secreted by fat cells (adipocytes)",
                    "Effect on food intake": "Reduces intake in proportion to the body's energy excess",
                    "Distinctive feature": "Circulates at high levels in obesity yet fails to curb appetite (resistance)"
                },
                "GLP-1": {
                    "Source": "Ileum and colon, in the presence of digested food",
                    "Effect on food intake": "Reduces food intake and stimulates insulin after glucose ingestion",
                    "Distinctive feature": "Incretin targeted by semaglutide and liraglutide"
                },
                "GIP": {
                    "Source": "Duodenum (mostly) and jejunum of the small intestine",
                    "Effect on food intake": "Reduces intake; boosts glucose-dependent insulin release",
                    "Distinctive feature": "Incretin targeted together with GLP-1 by tirzepatide"
                },
                "PYY": {
                    "Source": "Ileum and colon, alongside GLP-1 and CCK",
                    "Effect on food intake": "Reduces food intake after meals as a satiety signal",
                    "Distinctive feature": "Not an incretin; its fall after weight loss promotes regain"
                }
            }
        },
        {
            "slug": "mets_criteria",
            "title": "AHA/NHLBI Metabolic Syndrome Criteria",
            "subtitle": "Match each criterion (3 or more = metabolic syndrome) to its male cutoff, female cutoff, and how it is assessed",
            "categories": ["Cutoff in males", "Cutoff in females", "How it is assessed"],
            "data": {
                "Waist circumference": {
                    "Cutoff in males": ">40 inches",
                    "Cutoff in females": ">35 inches",
                    "How it is assessed": "Measured on physical examination"
                },
                "Blood pressure": {
                    "Cutoff in males": ">130 mm Hg systolic or >80 mm Hg diastolic",
                    "Cutoff in females": "Same cutoffs; antihypertensive therapy also counts",
                    "How it is assessed": "Office measurement or current medication list"
                },
                "Triglycerides": {
                    "Cutoff in males": ">150 mg/dL",
                    "Cutoff in females": ">150 mg/dL (same as males)",
                    "How it is assessed": "Fasting lipid profile"
                },
                "HDL cholesterol": {
                    "Cutoff in males": "<40 mg/dL",
                    "Cutoff in females": "<50 mg/dL",
                    "How it is assessed": "Fasting lipid profile (low value counts)"
                },
                "Glucose": {
                    "Cutoff in males": ">100 mg/dL",
                    "Cutoff in females": ">100 mg/dL (same as males)",
                    "How it is assessed": "Fasting serum glucose concentration"
                }
            }
        },
        {
            "slug": "obesity_drug_classes",
            "title": "Anti-Obesity Drug Classes",
            "subtitle": "Match each drug to its mechanism of action, adverse effects or cautions, and place in therapy",
            "categories": ["Mechanism of action", "Adverse effects / cautions", "Place in therapy"],
            "data": {
                "Semaglutide / liraglutide": {
                    "Mechanism of action": "GLP-1 receptor activation: satiety up, appetite down, slowed gastric emptying",
                    "Adverse effects / cautions": "Avoid with personal or family history of medullary thyroid carcinoma or MEN2",
                    "Place in therapy": "First-line options in conjunction with lifestyle modifications"
                },
                "Tirzepatide": {
                    "Mechanism of action": "Activates both GIP and GLP-1 receptors, improving glycemic signaling",
                    "Adverse effects / cautions": "Nausea, vomiting, delayed gastric emptying; rare gallbladder disease and pancreatitis",
                    "Place in therapy": "First-line dual-agonist option alongside lifestyle changes"
                },
                "Phentermine-topiramate ER": {
                    "Mechanism of action": "Sympathomimetic catecholamine signaling plus topiramate satiety effects",
                    "Adverse effects / cautions": "Caution in cardiovascular disease or uncontrolled hypertension; avoid in pregnancy",
                    "Place in therapy": "Second-line when incretin-based therapy is not appropriate or tolerated"
                },
                "Naltrexone-bupropion ER": {
                    "Mechanism of action": "Opioid antagonism plus increased NE/DA in hypothalamic appetite and reward pathways",
                    "Adverse effects / cautions": "Insomnia, dry mouth; avoid with seizure risk or chronic opioid use",
                    "Place in therapy": "Later-line, especially for craving/reward-driven eating"
                },
                "Orlistat": {
                    "Mechanism of action": "Inhibits gastric and pancreatic lipases, blocking dietary triglyceride absorption",
                    "Adverse effects / cautions": "Oily stools, fecal urgency, flatulence; reduced fat-soluble vitamin absorption",
                    "Place in therapy": "Older, less preferred nonsystemic oral option with modest efficacy"
                }
            }
        },
        {
            "slug": "sleeve_vs_rygb",
            "title": "Sleeve Gastrectomy vs Roux-en-Y Bypass",
            "subtitle": "Sort each feature under the correct bariatric procedure",
            "categories": ["Anatomic change", "Primary mechanism", "Key gut hormone effect", "Micronutrient deficiency risk"],
            "data": {
                "Sleeve gastrectomy": {
                    "Anatomic change": "Removes about 80% of the stomach, including the fundus",
                    "Primary mechanism": "Restrictive: volume reduction plus markedly reduced hunger signaling",
                    "Key gut hormone effect": "Decreased ghrelin, since the fundus is its primary source",
                    "Micronutrient deficiency risk": "Lower risk, but patients still require monitoring"
                },
                "Roux-en-Y gastric bypass": {
                    "Anatomic change": "Small 15-30 mL gastric pouch draining into a 75-150 cm Roux limb",
                    "Primary mechanism": "Restrictive plus some malabsorption from the bypassed segment",
                    "Key gut hormone effect": "Increased GLP-1 and PYY from rapid nutrient delivery to distal L-cells",
                    "Micronutrient deficiency risk": "Higher risk (iron, B12, calcium, vitamin D, folate); lifelong supplementation"
                }
            }
        }
    ]
}
