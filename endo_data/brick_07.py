BRICK = {
    "brick_num": 7,
    "brick_title": "Growth Hormone Deficiency and Excess",
    "games": [
        {
            "slug": "ghd_across_lifespan",
            "title": "GH Deficiency Across the Lifespan",
            "subtitle": "Sort each feature under the age group it belongs to",
            "categories": ["Why the deficiency is easy to miss", "Typical presentation", "What prompts the evaluation", "Usual cause", "Treatment"],
            "data": {
                "Newborn": {
                    "Why the deficiency is easy to miss": "Thyroid hormone drives growth for the first 2 years, so growth is normal",
                    "Typical presentation": "Hypoglycemia, prolonged jaundice, small genitalia, midline craniofacial defects",
                    "What prompts the evaluation": "Another sign such as neonatal hypoglycemia or ambiguous genitalia",
                    "Usual cause": "Congenital, including rare genetic and syndromic causes",
                    "Treatment": "Recombinant GH to support growth through infancy"
                },
                "Child": {
                    "Why the deficiency is easy to miss": "Commoner causes of growth failure mimic it and must be excluded first",
                    "Typical presentation": "Poor linear growth, doll-like facies, delayed bone age, motor delay",
                    "What prompts the evaluation": "Height more than 3 SD below expected or falling off the growth curve",
                    "Usual cause": "Most often idiopathic, sometimes tumor, trauma, radiation, or autoimmune",
                    "Treatment": "Recombinant GH until the epiphyseal plates are nearly closed"
                },
                "Adult": {
                    "Why the deficiency is easy to miss": "Symptoms are absent or look like ordinary age-related change",
                    "Typical presentation": "Low muscle mass, high fat mass, low bone density, more fractures",
                    "What prompts the evaluation": "Known hypothalamic-pituitary disease making deficiency likely",
                    "Usual cause": "Rare overall, and mostly caused by pituitary tumors",
                    "Treatment": "GH injections titrated by blood monitoring, with no height gain"
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
            "categories": ["Serum GH", "Serum IGF-1", "Underlying lesion", "Confirmatory test", "Treatment", "Growth pattern in a child"],
            "data": {
                "GH deficiency": {
                    "Serum GH": "Low, and fails to rise with provocative agents",
                    "Serum IGF-1": "Low, and the more useful screening value than GH",
                    "Underlying lesion": "Usually idiopathic; also tumor, trauma, radiation, or autoimmune damage",
                    "Confirmatory test": "GH stimulation test with L-dopa, clonidine, arginine, or glucagon",
                    "Treatment": "Recombinant GH injections",
                    "Growth pattern in a child": "Short stature with delayed bone age and high weight-to-height ratio"
                },
                "GH excess": {
                    "Serum GH": "High, and fails to fall after a glucose load",
                    "Serum IGF-1": "Elevated, and the best initial test for the disorder",
                    "Underlying lesion": "GH-secreting pituitary adenoma with somatotroph hyperplasia",
                    "Confirmatory test": "GH suppression test using an oral glucose load",
                    "Treatment": "Surgical resection of the adenoma, then medical therapy",
                    "Growth pattern in a child": "Excessive linear growth, usually recognized around puberty"
                },
                "Laron syndrome": {
                    "Serum GH": "High, because low IGF-1 removes feedback inhibition",
                    "Serum IGF-1": "Low despite plentiful circulating GH",
                    "Underlying lesion": "Autosomal recessive mutation of the GH receptor",
                    "Confirmatory test": "Genetic analysis showing the GH receptor mutation",
                    "Treatment": "Recombinant IGF-1 injections, since GH cannot work",
                    "Growth pattern in a child": "Severe growth failure with prominent forehead and saddle nose"
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
