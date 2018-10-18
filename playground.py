import smelli
import ipywidgets as widgets
import wcxf
import yaml

# allowed bases
# WET: everything that can be translated to flavio
bases_wet = ['flavio'] + [f for eft,f, t in wcxf.Basis['WET', 'flavio'].known_translators['to']]
# SMEFT: everything that can be matched onto JMS
bases_smeft = ['Warsaw'] + [b1 for eft1, b1, eft2, b2 in wcxf.Matcher.instances
                            if eft1 == 'SMEFT' and eft2 == 'WET' and b2 == 'JMS'
                            and b1 != 'Warsaw']
eft_bases = {'SMEFT': bases_smeft, 'WET': bases_wet}

gl = None


def print_basis(basis):
    pass

def f_basis(eft):
    select_basis.options = eft_bases[eft]


select_eft = widgets.Select(options=['SMEFT', 'WET'])
init = select_eft.value
select_basis = widgets.Select(options=eft_bases[init])

widget_basis = widgets.interactive(print_basis, basis=select_basis)
widget_eft = widgets.interactive(f_basis, eft=select_eft)

def read_yaml(s):
    if not s:
        return {}
    d = yaml.load(s)
    return {k: complex(v) if isinstance(v, str) else v for k, v in d.items()}

ta_wc = widgets.Textarea(description="Wilson coefficients",
                         layout=widgets.Layout(min_width='50%', height='300px'),
                         style={'description_width': 'initial'})
t_scale = widgets.Text(description="Scale in GeV", value='91.1876')
