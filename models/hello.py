import logging
from odoo import models, fields, api, _
# from slugify import slugify
from odoo.addons.http_routing.models.ir_http import slugify
from datetime import datetime

_logger = logging.getLogger(__name__)
# _logger.setLevel('INFO')


class Course(models.Model):
    _name = 'openacademy.course'
    _description = "OpenAcademy Courses"

    name = fields.Char(string="Title", required=True)
    description = fields.Text()
    parent_id = fields.Many2one('openacademy.course', required=False, ondelete='cascade')
    name_tree = fields.Char(compute='compute_name_tree', store=True, default='/')

    parent_ids = fields.Many2many(
        comodel_name  = 'openacademy.course',
        relation = 'ids',
        column1 = 'parent_ids',
        column2 = 'child_ids')


    # def write(self, value):
    #     super().write(value)
    #     for record in self:
    #         record.compute_name_tree()
    #serch function
    # def find_elem(self, operator, value):
    #     element = self.search([]).filtered(lambda x: value in x.name_tree)
    #     if element:
    #         return [('id', 'in', element.ids)]

    @api.depends('parent_id', 'name_tree', 'name')
    def compute_name_tree(self):
        for record in self:
            if record.parent_id.name_tree:
                record.name_tree = str(record.parent_id.name_tree) + '/' + record.name
            else:record.name_tree = '/' + str(record.name)


    @api.onchange('name', 'description')
    def _onchange_name(self):
        self.description = slugify(self.name)+'-'+str(datetime.now())

    status_selection = fields.Selection(string='Communication',
        selection=[
            ('upselling', 'Upselling Opportunity'),
            ('invoiced', 'Fully Invoiced'),
            ('to invoice', 'To Invoice')], default='upselling',
        help='You can set here the communication type that will appear on sales orders.'
             'The communication will be given to the customer when they choose the payment method.')

    def next_element_action(self):
        _logger.info("X: %s", self.status_selection)
        if self.status_selection == 'upselling':
            self.status_selection = 'invoiced'
        elif self.status_selection == 'invoiced':
            self.status_selection = 'to invoice'
        elif self.status_selection == 'to invoice':
            self.status_selection = 'upselling'
    def back_element_action(self):
        _logger.info("X: %s", self.status_selection)
        if self.status_selection == 'upselling':
            self.status_selection = 'to invoice'
        elif self.status_selection == 'invoiced':
            self.status_selection = 'upselling'
        elif self.status_selection == 'to invoice':
            self.status_selection = 'invoiced'
