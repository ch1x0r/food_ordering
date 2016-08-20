saved_orders = [
	"1) 1 lb wimpy",
	"2) 1 lb wimpy garlic parm",
	"3) 1 lb wimpy spicy teriyaki",
	"4) hangar 1 wimpy sprite",
	"5) hangar 1 wimpy garlic parm sprite",
	"6) hangar 1 wimpy spicy teriyaki sprite",
	]
	
order_instructions = {
	'1': ['#mnuitems > form:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(4) > a:nth-child(1)',
			'#id116186294633720', 'li.TabbedPanelsTab:nth-child(2)', '#id116185794632690', '#itemdetails > form:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > a:nth-child(2)',
			'.review-order'],
	'2': ['#mnuitems > form:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(4) > a:nth-child(1)',
			'#id116186294633720', '#id116186294633630', 'li.TabbedPanelsTab:nth-child(2)', '#id116185794632690', '#itemdetails > form:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > a:nth-child(2)',
			'.review-order'],
	'3': ['#mnuitems > form:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(4) > a:nth-child(1)',
			'#id116186294633720', '#id116186294633580', 'li.TabbedPanelsTab:nth-child(2)', '#id116185794632690', '#itemdetails > form:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > a:nth-child(2)',
			'.review-order'],
	'4': ['li.menulist_menu_name_link:nth-child(4) > a:nth-child(1)', '#mnuitems > form:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(4) > a:nth-child(1)',
			'#id116186294633720', 'li.TabbedPanelsTab:nth-child(2)', '#id116188094635950', 'li.TabbedPanelsTab:nth-child(4)', '#id116188194636020', '#itemdetails > form:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > a:nth-child(2)',
			'.review-order'],
	'5': ['li.menulist_menu_name_link:nth-child(4) > a:nth-child(1)', '#mnuitems > form:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(4) > a:nth-child(1)',
			'#id116186294633720', '#id116186294633630', 'li.TabbedPanelsTab:nth-child(2)', '#id116188094635950', 'li.TabbedPanelsTab:nth-child(4)','#id116188194636020', '#itemdetails > form:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > a:nth-child(2)',
			'.review-order'],
	'6': ['li.menulist_menu_name_link:nth-child(4) > a:nth-child(1)', '#mnuitems > form:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(4) > a:nth-child(1)',
			'#id116186294633720', '#id116186294633580', 'li.TabbedPanelsTab:nth-child(2)', '#id116188094635950', 'li.TabbedPanelsTab:nth-child(4)', '#id116188194636020', '#itemdetails > form:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2) > a:nth-child(2)',
			'.review-order'],
}

confirm_order= {
	'1': '#ordreview > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > form:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(26) > td:nth-child(1) > a:nth-child(4)',
	'2': '#ordreview > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > form:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(27) > td:nth-child(1) > a:nth-child(4)',
	'3': '#ordreview > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > form:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(27) > td:nth-child(1) > a:nth-child(4)', 
	'4': '#ordreview > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > form:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(29) > td:nth-child(1) > a:nth-child(4)', 
	'5': '#ordreview > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > form:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(30) > td:nth-child(1) > a:nth-child(4)',
	'6': '#ordreview > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > form:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(30) > td:nth-child(1) > a:nth-child(4)',
}

cost_matrix= {
	'1': '$13.90', 
	'2': '$13.90', 
	'3': '$13.90', 
	'4': '$15.50', 
	'5': '$15.50',
	'6': '$15.50',
}
