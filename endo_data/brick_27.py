BRICK = {
    "brick_num": 27,
    "brick_title": "Treatment of Diabetes with Glucose-Lowering Agents",
    "games": [
        {
            "slug": "insulin_formulations",
            "title": "Insulin Formulations by Pharmacokinetics",
            "subtitle": "Match each insulin preparation to its timing class, its distinguishing pharmacologic feature, and its clinical role",
            "categories": ["Timing class", "Distinguishing feature", "Clinical role"],
            "data": {
                "Insulin aspart": {
                    "Timing class": "Rapid-acting, given up to 15 minutes before meals",
                    "Distinguishing feature": "Fastest onset of the analogs; the insulin used in pumps",
                    "Clinical role": "Bolus mealtime coverage in a basal-bolus regimen"
                },
                "Regular insulin": {
                    "Timing class": "Short-acting, given 30-60 minutes before meals",
                    "Distinguishing feature": "The only formulation that can be given intravenously",
                    "Clinical role": "DKA, hyperosmolar hyperglycemic state, severe hyperkalemia"
                },
                "NPH insulin": {
                    "Timing class": "Intermediate-acting basal insulin",
                    "Distinguishing feature": "Regular insulin complexed with protamine and zinc to delay absorption",
                    "Clinical role": "Subcutaneous basal control only; never used for rapid lowering"
                },
                "Insulin glargine": {
                    "Timing class": "Long-acting, dosed once daily",
                    "Distinguishing feature": "Low isoelectric point precipitates in subcutaneous tissue; may sting",
                    "Clinical role": "Flat, peakless basal coverage between meals and overnight"
                },
                "Insulin degludec": {
                    "Timing class": "Ultra-long-acting, dosed once daily",
                    "Distinguishing feature": "Forms multihexamers that create a slowly released depot",
                    "Clinical role": "Longest duration of the daily basal insulins"
                },
                "Insulin icodec": {
                    "Timing class": "Ultra-long-acting, dosed once weekly",
                    "Distinguishing feature": "Strong albumin binding stretches release over about one week",
                    "Clinical role": "Weekly basal option when injection burden limits adherence"
                }
            }
        },
        {
            "slug": "noninsulin_classes",
            "title": "Non-Insulin Glucose-Lowering Classes",
            "subtitle": "Match each drug class to its example agents, its mechanism, and the adverse effect it is known for",
            "categories": ["Example agents", "Mechanism", "Characteristic adverse effect"],
            "data": {
                "Biguanides": {
                    "Example agents": "Metformin",
                    "Mechanism": "Promotes GLUT-4 translocation, lowers gluconeogenesis and gut glucose absorption",
                    "Characteristic adverse effect": "GI upset and metallic taste; rare but fatal lactic acidosis"
                },
                "Thiazolidinediones": {
                    "Example agents": "Pioglitazone, rosiglitazone",
                    "Mechanism": "Activate nuclear PPAR-gamma so cells store fatty acids and burn glucose",
                    "Characteristic adverse effect": "Fluid retention, edema, heart failure, fractures, weight gain"
                },
                "GLP-1 receptor agonists": {
                    "Example agents": "Liraglutide, exenatide, semaglutide",
                    "Mechanism": "Gs-coupled GLP-1 receptor raises beta-cell cAMP and suppresses glucagon",
                    "Characteristic adverse effect": "GI upset and acute pancreatitis"
                },
                "Sulfonylureas": {
                    "Example agents": "Glipizide, glyburide",
                    "Mechanism": "Close ATP-sensitive K+ channels, depolarizing beta cells to release insulin",
                    "Characteristic adverse effect": "Hypoglycemia and weight gain"
                },
                "SGLT2 inhibitors": {
                    "Example agents": "Empagliflozin, dapagliflozin, canagliflozin",
                    "Mechanism": "Block proximal tubule glucose reabsorption so glucose spills into urine",
                    "Characteristic adverse effect": "Genital candidiasis, UTIs, dehydration, euglycemic DKA"
                },
                "Alpha-glucosidase inhibitors": {
                    "Example agents": "Acarbose, miglitol",
                    "Mechanism": "Inhibit intestinal brush-border enzymes that digest complex carbohydrates",
                    "Characteristic adverse effect": "Bloating and flatulence, eased by slow dose titration"
                }
            }
        },
        {
            "slug": "secretagogue_compare",
            "title": "Three Ways to Raise Insulin Secretion",
            "subtitle": "Sort each feature under the insulin-releasing drug class it describes",
            "categories": ["Relationship to incretin signaling", "Route of administration", "Hypoglycemia risk", "Effect on body weight", "Serious adverse effect", "Best clinical niche"],
            "data": {
                "GLP-1 receptor agonists": {
                    "Relationship to incretin signaling": "Directly bind and activate the GLP-1 receptor as incretin mimetics",
                    "Route of administration": "Subcutaneous injection, some lasting up to a week",
                    "Hypoglycemia risk": "Rare, because insulin release stays glucose-dependent",
                    "Effect on body weight": "Weight loss from satiety and delayed gastric emptying",
                    "Serious adverse effect": "Acute pancreatitis on top of common GI upset",
                    "Best clinical niche": "Obesity with coronary artery disease or HbA1c above 9% on metformin"
                },
                "DPP-4 inhibitors": {
                    "Relationship to incretin signaling": "Block the enzyme that degrades GLP-1, raising endogenous incretin levels",
                    "Route of administration": "Oral gliptins such as sitagliptin and linagliptin",
                    "Hypoglycemia risk": "Minimal; generally well tolerated in this respect",
                    "Effect on body weight": "Weight neutral",
                    "Serious adverse effect": "Hypersensitivity, severe joint pain; saxagliptin and HF hospitalization",
                    "Best clinical niche": "Add-on therapy when a modest, well-tolerated drop is enough"
                },
                "Sulfonylureas": {
                    "Relationship to incretin signaling": "None; they act on the beta-cell K+ channel independent of incretins",
                    "Route of administration": "Oral, inexpensive, and long time-tested",
                    "Hypoglycemia risk": "High, and the main reason they fell to second- or third-line",
                    "Effect on body weight": "Weight gain from increased insulin and fat storage",
                    "Serious adverse effect": "Confusion, falls, coma, and early-onset dementia in the elderly",
                    "Best clinical niche": "Cost-limited patients who are not prone to hypoglycemia"
                }
            }
        },
        {
            "slug": "who_gets_what",
            "title": "Picking the Drug for the Patient",
            "subtitle": "Match each agent to the patient who benefits, the patient who should avoid it, and the reason",
            "categories": ["Patient who benefits", "Patient who should avoid it", "Reason for the caution"],
            "data": {
                "Metformin": {
                    "Patient who benefits": "Most newly diagnosed type 2 diabetics, especially if obese",
                    "Patient who should avoid it": "eGFR under 30, severe heart failure, or progressive liver disease",
                    "Reason for the caution": "These states predispose to rare but fatal lactic acidosis"
                },
                "Pioglitazone": {
                    "Patient who benefits": "Patient who cannot tolerate or take metformin",
                    "Patient who should avoid it": "Patient with heart failure or bladder cancer risk factors",
                    "Reason for the caution": "PPAR-gamma raises collecting-tubule sodium reabsorption and fluid retention"
                },
                "Empagliflozin": {
                    "Patient who benefits": "Patient with cardiovascular disease who also needs weight loss",
                    "Patient who should avoid it": "Recurrent urinary infections or eGFR under 45",
                    "Reason for the caution": "Glycosuria feeds infection and the drug needs decent renal function"
                },
                "Glyburide": {
                    "Patient who benefits": "Patient needing an inexpensive oral option, including in pregnancy",
                    "Patient who should avoid it": "Elderly patient with CKD or recurrent hypoglycemic episodes",
                    "Reason for the caution": "Reduced excretion and a long half-life prolong the insulin surge"
                },
                "Semaglutide": {
                    "Patient who benefits": "Obese patient still above 9% HbA1c despite metformin",
                    "Patient who should avoid it": "Patient who refuses injections or has had pancreatitis",
                    "Reason for the caution": "It is subcutaneous only and can trigger acute pancreatitis"
                },
                "Insulin": {
                    "Patient who benefits": "Type 1 diabetes, pregnancy, or marked hyperglycemia from insulin deficiency",
                    "Patient who should avoid it": "Type 2 patient still controllable on non-insulin agents",
                    "Reason for the caution": "Weight gain worsens resistance, and fasting hypoglycemia can be fatal"
                }
            }
        }
    ]
}
