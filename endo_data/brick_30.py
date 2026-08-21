BRICK = {
    "brick_num": 30,
    "brick_title": "Chronic Complications of Diabetes Mellitus",
    "games": [
        {
            "slug": "hyperglycemic_damage_pathways",
            "title": "How Hyperglycemia Damages Tissue",
            "subtitle": "Match each biochemical step to what it does to the cell and why it matters clinically",
            "categories": ["Chemical step", "Cellular consequence", "Clinical relevance"],
            "data": {
                "Sorbitol accumulation": {
                    "Chemical step": "Excess intracellular glucose is reduced to sorbitol",
                    "Cellular consequence": "Osmotic stress and swelling plus depletion of cellular antioxidants",
                    "Clinical relevance": "Drives lens swelling and cataract formation in diabetic eye disease"
                },
                "Fructose generation": {
                    "Chemical step": "The polyol pathway converts sorbitol onward to fructose",
                    "Cellular consequence": "Fructose promotes formation of advanced glycation end products",
                    "Clinical relevance": "Links polyol pathway flux to AGE-mediated tissue damage"
                },
                "Nonenzymatic glycation": {
                    "Chemical step": "Glucose attaches to proteins and lipids without any enzyme",
                    "Cellular consequence": "Early glycation products are reversible until hyperglycemia persists",
                    "Clinical relevance": "Sustained high glucose locks in irreversible AGEs"
                },
                "Collagen cross-linking": {
                    "Chemical step": "AGEs cross-link collagen molecules to one another",
                    "Cellular consequence": "Tissue stiffening with loss of normal compliance",
                    "Clinical relevance": "Contributes to vessel wall and connective tissue dysfunction"
                },
                "RAGE receptor binding": {
                    "Chemical step": "AGEs bind RAGE receptors on the cell surface",
                    "Cellular consequence": "Triggers oxidative stress and inflammatory signaling",
                    "Clinical relevance": "Underlies endothelial dysfunction in retina, nerve, and vessels"
                },
                "Glycated hemoglobin": {
                    "Chemical step": "Blood glucose binds hemoglobin inside circulating red cells",
                    "Cellular consequence": "A stable modification that persists for the cell's life",
                    "Clinical relevance": "HbA1c reflects average glucose over roughly 120 days"
                }
            }
        },
        {
            "slug": "npdr_vs_pdr",
            "title": "Non-Proliferative vs Proliferative Retinopathy",
            "subtitle": "Sort each feature into the stage of diabetic retinopathy it belongs to",
            "categories": ["Defining vascular change", "Fundoscopic findings", "Earliest or defining lesion", "Key mediator", "How vision is lost", "Targeted management"],
            "data": {
                "Non-proliferative (NPDR)": {
                    "Defining vascular change": "Retinal microvascular damage without abnormal new vessel growth",
                    "Fundoscopic findings": "Microaneurysms, intraretinal hemorrhages, cotton-wool spots, hard exudates",
                    "Earliest or defining lesion": "Microaneurysms from pericyte loss appear first in mild disease",
                    "Key mediator": "Sorbitol, AGE-RAGE injury, and basement membrane thickening",
                    "How vision is lost": "Macular edema blurs acuity and can occur at any stage",
                    "Targeted management": "Glycemic and blood pressure control with yearly dilated exams"
                },
                "Proliferative (PDR)": {
                    "Defining vascular change": "Neovascularization arising from the optic disc or retinal vessels",
                    "Fundoscopic findings": "Fragile new vessels at the disc or along retinal vessels",
                    "Earliest or defining lesion": "Capillary closure and retinal ischemia precede the new vessels",
                    "Key mediator": "Hypoxia-driven VEGF, with IGF-1 and other growth factors",
                    "How vision is lost": "Vitreous hemorrhage, fibrosis, and tractional retinal detachment",
                    "Targeted management": "Laser photocoagulation to inhibit vessel proliferation"
                }
            }
        },
        {
            "slug": "neuropathy_syndromes",
            "title": "Syndromes of Diabetic Neuropathy",
            "subtitle": "Match each neuropathic complication to how it presents, why it happens, and how it is managed",
            "categories": ["Clinical presentation", "Mechanism", "Management"],
            "data": {
                "Peripheral sensory neuropathy": {
                    "Clinical presentation": "Foot pain, tingling, and numbness in a stocking-glove distribution",
                    "Mechanism": "Sorbitol and AGE-RAGE injury demyelinate and atrophy nerve fibers",
                    "Management": "Pregabalin, gabapentin, or duloxetine for pain; sensation is not restored"
                },
                "Diabetic foot ulcer": {
                    "Clinical presentation": "Painless open wound that heals poorly and becomes infected",
                    "Mechanism": "Unnoticed injury from sensory loss plus impaired blood flow",
                    "Management": "Daily foot inspection, well-fitting footwear, never walking barefoot"
                },
                "Charcot foot": {
                    "Clinical presentation": "Warm, red foot or ankle with progressive destructive deformity",
                    "Mechanism": "Unnoticed repetitive microtrauma drives bone resorption and joint collapse",
                    "Management": "Casting initially, followed by orthopedic footwear"
                },
                "Orthostatic hypotension": {
                    "Clinical presentation": "Lightheadedness on standing, leading to falls and fractures",
                    "Mechanism": "Impaired sympathetic activation of vascular smooth muscle contraction",
                    "Management": "Compression stockings and resistance exercise; midodrine if severe"
                },
                "Diabetic gastroparesis": {
                    "Clinical presentation": "Nausea, vomiting, anorexia, and weight loss from delayed emptying",
                    "Mechanism": "Autonomic damage decreases gastrointestinal motility",
                    "Management": "Small low-fat, low-fiber meals; metoclopramide short-term if needed"
                }
            }
        },
        {
            "slug": "cv_risk_management",
            "title": "Preventing Macrovascular Disease in Diabetes",
            "subtitle": "Match each intervention to who receives it, the target or agent, and the reason behind it",
            "categories": ["Who receives it", "Target or agent", "Reason"],
            "data": {
                "Glycemic control": {
                    "Who receives it": "Most patients with diabetes mellitus",
                    "Target or agent": "Hemoglobin A1c below 7%",
                    "Reason": "Prevents or delays both macrovascular and microvascular complications"
                },
                "Antiplatelet therapy": {
                    "Who receives it": "Patients with established coronary artery disease",
                    "Target or agent": "Low-dose aspirin, or clopidogrel as an alternative",
                    "Reason": "Clopidogrel may be equally effective with fewer side effects"
                },
                "Statin therapy": {
                    "Who receives it": "Adults aged 40 to 70 regardless of baseline LDL",
                    "Target or agent": "Moderate-intensity statin",
                    "Reason": "Prevents coronary artery disease and other cardiovascular events"
                },
                "Blood pressure control": {
                    "Who receives it": "Patients with diabetes and known or high-risk cardiovascular disease",
                    "Target or agent": "Below 130/80 mm Hg, starting with an ACE inhibitor",
                    "Reason": "Hypertension potentiates endothelial dysfunction and atherosclerosis"
                },
                "ACE inhibitor for proteinuria": {
                    "Who receives it": "Patients with diabetes who have proteinuria",
                    "Target or agent": "ACE inhibitor, or an ARB, with an SGLT2 inhibitor when indicated",
                    "Reason": "Blocking angiotensin II protects the heart, kidneys, and possibly the eyes"
                },
                "Exercise ECG testing": {
                    "Who receives it": "Patients with vague chest pain, dyspnea, or an abnormal resting ECG",
                    "Target or agent": "Exercise stress test or an equivalent study",
                    "Reason": "Screens for coronary disease that is often silent in diabetes"
                }
            }
        }
    ]
}
