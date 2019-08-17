from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, FloatField, SelectField, SubmitField, DateField
import datetime

class Ticket(FlaskForm):
	book1 = SelectField('Book1', choices=[('DTBJ', 'MQF.DTBJ'), ('CLOF', 'MQF.CLOF'), ('CLOS', 'MQF.CLOS'), ('2119', 'MQF.2119')])
	book2 = SelectField('Book2', choices=[('DTBJ', 'MQF.DTBJ'), ('CLOF', 'MQF.CLOF'), ('CLOS', 'MQF.CLOS'), ('2119', 'MQF.2119')])
	account = StringField('Account')
	bond = StringField('Bond')
	quantity = FloatField('Quantity')
	buysell = SelectField('Transaction', choices=[('Buy', 'Buy'), ('Sell', 'Sell')])
	trade_date = DateField('Trade Date', default=datetime.date.today(), format='%m/%d/%Y')
	settle_date = DateField('Settle Date', format='%m/%d/%Y')
	book_trade = SubmitField('Book Trade')
	book_trades = SubmitField('Bool Bulk Trades')
	num_trades = IntegerField('Number of trades')
	
	
