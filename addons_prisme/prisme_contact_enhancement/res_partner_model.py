from osv import fields, osv

class res_partner(osv.osv):
    _name = 'res.partner'
    _inherit = 'res.partner'

    _columns = {

                'prescriber': fields.many2one('res.partner', 'Prescriber'),

                }


res_partner()
