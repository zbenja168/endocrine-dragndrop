BRICK = {
    "brick_num": 7,
    "brick_title": "Growth Hormone Deficiency and Excess",
    "games": [
        {
            "slug": "ghd_across_lifespan",
            "title": "GH Deficiency Across the Lifespan",
            "subtitle": "Sort each feature under the age group it belongs to",
            "categories": ["Newborn", "Child", "Adult"],
            "data": {
                "Why the deficiency is easy to miss": {
                    "Newborn": "Thyroid hormone drives growth for the first 2 years, so growth is normal",
                    "Child": "Commoner causes of growth failure mimic it and must be excluded first",
                    "Adult": "Symptoms are absent or look like ordinary age-related change"
                },
                "Typical presentation": {
                    "Newborn": "Hypoglycemia, prolonged jaundice, small genitalia, midline craniofacial defects",
                    "Child": "Poor linear growth, doll-like facies, delayed bone age, motor delay",
                    "Adult": "Low muscle mass, high fat mass, low bone density, more fractures"
                },
                "What prompts the evaluation": {
                    "Newborn": "Another sign such as neonatal hypoglycemia or ambiguous genitalia",
                    "Child": "Height more than 3 SD below expected or falling off the growth curve",
                    "Adult": "Known hypothalamic-pituitary disease making deficiency likely"
                },
                "Usual cause": {
                    "Newborn": "Congenital, including rare genetic and syndromic causes",
                    "Child": "Most often idiopathic, sometimes tumor, trauma, radiation, or autoimmune",
                    "Adult": "Rare overall, and mostly caused by pituitary tumors"
                },
                "Treatment": {
                    "Newborn": "Recombinant GH to support growth through infancy",
                    "Child": "Recombinant GH until the epiphyseal plates are nearly closed",
                    "Adult": "GH injections titrated by blood monitoring, with no height gain"
                }
            }
        },
        {
            "slug": "gh_actions",
            "title": "Actions of Growth Hormone",
            "subtitle": "Match each GH action to its tissue, its immediate effect, and its clinical consequence",
            "categories": ["Tissue", "Immediate effect", "Clinical consequence"],
            "data": {
                "IGF-1 generation": {
                    "Tissue": "Liver, stimulated directly by circulating GH",
                    "Immediate effect": "Releases IGF-1, the main mediator of bone and tissue growth",
                    "Clinical consequence": "IGF-1 is the screening test because GH itself is pulsatile"
                },
                "Epiphyseal plate stimulation": {
                    "Tissue": "Growth plates of the long bones",
                    "Immediate effect": "Drives linear growth and increases bone mineralization",
                    "Clinical consequence": "Excess before plate fusion produces gigantism"
                },
                "Muscle hypertrophy": {
                    "Tissue": "Skeletal muscle",
                    "Immediate effect": "Increases muscle bulk by hypertrophy of existing fibers",
                    "Clinical consequence": "Deficiency lowers muscle mass; replacement restores it"
                },
                "Gluconeogenesis and insulin antagonism": {
                    "Tissue": "Liver and insulin-sensitive peripheral tissue",
                    "Immediate effect": "Raises serum glucose by opposing the action of insulin",
                    "Clinical consequence": "Chronic excess causes secondary diabetes mellitus"
                },
                "Lipolysis and lipid oxidation": {
                    "Tissue": "Adipose tissue",
                    "Immediate effect": "Breaks down stored fat and raises free fatty acids",
                    "Clinical consequence": "Replacement lowers fat mass; excess speeds atherosclerosis"
                }
            }
        },
        {
            "slug": "gh_lab_patterns",
            "title": "Sorting Out the GH Axis Disorders",
            "subtitle": "Sort each finding under the disorder it belongs to",
            "categories": ["GH deficiency", "GH excess", "Laron syndrome"],
            "data": {
                "Serum GH": {
                    "GH deficiency": "Low, and fails to rise with provocative agents",
                    "GH excess": "High, and fails to fall after a glucose load",
                    "Laron syndrome": "High, because low IGF-1 removes feedback inhibition"
                },
                "Serum IGF-1": {
                    "GH deficiency": "Low, and the more useful screening value than GH",
                    "GH excess": "Elevated, and the best initial test for the disorder",
                    "Laron syndrome": "Low despite plentiful circulating GH"
                },
                "Underlying lesion": {
                    "GH deficiency": "Usually idiopathic; also tumor, trauma, radiation, or autoimmune damage",
                    "GH excess": "GH-secreting pituitary adenoma with somatotroph hyperplasia",
                    "Laron syndrome": "Autosomal recessive mutation of the GH receptor"
                },
                "Confirmatory test": {
                    "GH deficiency": "GH stimulation test with L-dopa, clonidine, arginine, or glucagon",
                    "GH excess": "GH suppression test using an oral glucose load",
                    "Laron syndrome": "Genetic analysis showing the GH receptor mutation"
                },
                "Treatment": {
                    "GH deficiency": "Recombinant GH injections",
                    "GH excess": "Surgical resection of the adenoma, then medical therapy",
                    "Laron syndrome": "Recombinant IGF-1 injections, since GH cannot work"
                },
                "Growth pattern in a child": {
                    "GH deficiency": "Short stature with delayed bone age and high weight-to-height ratio",
                    "GH excess": "Excessive linear growth, usually recognized around puberty",
                    "Laron syndrome": "Severe growth failure with prominent forehead and saddle nose"
                }
            }
        },
        {
            "slug": "acromegaly_therapy",
            "title": "Treating GH Excess",
            "subtitle": "Match each therapy to its mechanism, its site of action, and its main caveat",
            "categories": ["Mechanism", "Site of action", "Main caveat"],
            "data": {
                "Surgical resection": {
                    "Mechanism": "Removes the hormone-producing tumor outright",
                    "Site of action": "The GH-secreting pituitary adenoma itself",
                    "Main caveat": "First-line therapy; soft tissue changes revert only gradually"
                },
                "Octreotide": {
                    "Mechanism": "Somatostatin analog activating inhibitory receptors",
                    "Site of action": "Somatotrophs of the anterior pituitary",
                    "Main caveat": "Lowers GH and IGF-1 and may also shrink the adenoma"
                },
                "Cabergoline": {
                    "Mechanism": "Dopamine receptor agonist suppressing GH release",
                    "Site of action": "Dopamine receptors on some somatotroph adenomas",
                    "Main caveat": "Most useful when residual IGF-1 elevation is only mild"
                },
                "Pegvisomant": {
                    "Mechanism": "Blocks GH receptors so GH signaling cannot occur",
                    "Site of action": "Peripheral target tissues, not the pituitary",
                    "Main caveat": "Tumor size must be followed separately by imaging"
                },
                "Radiation therapy": {
                    "Mechanism": "Irradiates residual hormone-producing tumor tissue",
                    "Site of action": "The sella and any remaining adenoma",
                    "Main caveat": "Reserved for disease surgery and drugs cannot control"
                }
            }
        }
    ]
}
