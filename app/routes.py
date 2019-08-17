from flask import render_template, flash, redirect, url_for
from app import app, mongo
from app.ticket import Ticket
from bson.objectid import ObjectId
import datetime

@app.route('/')
@app.route('/index')
@app.route('/index/<obj_id>')
def index(obj_id=None):
	msg = 'Hello, World!'
	if obj_id:
		record = mongo.db.trade_table.find_one({"_id": ObjectId(obj_id)})
		msg = 'Trade Booked!\nBook1:{}\nBook2:{}\nAccount:{}\nBond:{}\nQuantity:{}\n BuySell:{}\nTrade Date:{}\nSettle Date:{}'.format(record['Book1'], record['Book2'], record['Account'], record['Bond'], record['Quantity'], record['BuySell'], record['TradeDate'], record['SettleDate'])
	return msg

@app.route('/ticket', methods=['GET', 'POST'])
def ticket():
	form = Ticket()
	if form.is_submitted():
		if form.book_trade.data:
			objid = mongo.db.trade_table.insert_one({
				'Book1': form.book1.data,
				'Book2': form.book2.data,
				'Account': form.account.data,
				'Bond': form.bond.data,
				'Quantity': form.quantity.data,
				'BuySell': form.buysell.data,
				'TradeDate': str(form.trade_date.data),
				'SettleDate': str(form.settle_date.data)
			})
			return redirect(url_for('index', obj_id=objid.inserted_id))
		elif form.book_trades.data:
			result = _bulkBookings(form.num_trades.data)
			msgs = []
			for i in result.inserted_ids:
				record = mongo.db.trade_table.find_one({"_id": i})
				msg = 'Book1:{}, Book2:{}, Account:{}, Bond:{}, Quantity:{}, BuySell:{}, Trade Date:{}, Settle Date:{}'.format(
					record['Book1'],
					record['Book2'],
					record['Account'],
					record['Bond'],
					record['Quantity'],
					record['BuySell'],
					record['TradeDate'],
					record['SettleDate']
				)
				msgs.append(msg)
			return '\n'.join(msgs)
	return render_template('ticket.html', product='ABS', form=form)

def _bulkBookings(num_trades):
	records = []
	buysell = ['Buy', 'Sell']
	for i in range(num_trades):
		records.append({
			'Book1': 'BOOK1_{0}'.format(i),
			'Book2': 'BOOK2_{0}'.format(i),
			'Account': 'ACCOUNT_{0}'.format(i),
			'Bond': 'BOND_{0}'.format(i),
			'Quantity': 1000+i,
			'BuySell': buysell[i%2],
			'TradeDate': str(datetime.date.today()),
			'SettleDate': str(datetime.date(2020, 8, 22))
		})
	result = mongo.db.trade_table.insert_many(records)
	return result
