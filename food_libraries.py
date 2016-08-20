saved_orders = [] #populate with data matching the syntax described in the CL output.




flavors_matrix= {
'barbeque': '#id116186294633540',
'cajun barbeque': '#id116186294633600',
'sweet onion barbecue': '#id116186294633610',
'kickin barbecue': '#id116186294633560',
'spicy teriyaki': '#id116186294633580',
'honey mustard': '#id116186294633620',
'jamaican jerk': '#id116186294633640',
'west texas mesquite': '#id116186294633660',
'hot garlic': '#id116186294633690',
'plain': '#id116186294633710',
'cruisin buffalo': '#id116186294633730',
'jet fuel buffalo': '#id116186294633750',
'srirachayaki': '#id116186294633780',
'honey barbecue': '#id116186294633550',
'golden barbecue': '#id116186294633590',
'chipotle barbeque': '#id116186294633770',
'teriyaki': '#id116186294633570',
'cajun teriyaki': '#id116186294633680',
'garlic parmesean': '#id116186294633630',
'cajun blackened': '#id116186294633650',
'sweet chili': '#id116186294633670',
'mustang ranch': '#id116186294633700',
'wimpy buffalo': '#id116186294633720',
'red alert buffalo': '#id116186294633740',
'afterburner buffalo': '#id116186294633760',
'mango habanero': '#id116186294633790',
}

dressings_matrix= {
    'bleu cheese': '#id116185794632700',
    'ranch': '#id116185794632690',
    'no dressing': '#id116185794632700',
}

waffle_fries_matrix= {
'waffle cajun blackened' : '#id116189794637470',
'waffle west texas mesquite': '#id116189794637480',
'waffle mustang ranch' : '#id116189794637490',
'waffle garlic parmasean': '#id116189794637500',
'waffle plain': '#id116189794637510'
}

drink_matrix= {
'coke': '#mnuitems > form:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(4) > a:nth-child(1) > img:nth-child(1)',
'diet coke': '#mnuitems > form:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(4) > a:nth-child(1) > img:nth-child(1)',
'sprite' : '#mnuitems > form:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(5) > td:nth-child(4) > a:nth-child(1) > img:nth-child(1)',
'ice tea': '#mnuitems > form:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(7) > td:nth-child(4) > a:nth-child(1) > img:nth-child(1)',
'fanta grape': '#mnuitems > form:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(9) > td:nth-child(4) > a:nth-child(1) > img:nth-child(1)',
'root beer': '#mnuitems > form:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(4) > a:nth-child(1) > img:nth-child(1)',
'cherry coke': '#mnuitems > form:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(13) > td:nth-child(4) > a:nth-child(1) > img:nth-child(1)',
'dr. pepper': '#mnuitems > form:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(15) > td:nth-child(4) > a:nth-child(1) > img:nth-child(1)',
'fanta oranga': '#mnuitems > form:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(17) > td:nth-child(4) > a:nth-child(1) > img:nth-child(1)',
}

boneless_matrix= {
'.5': '#mnuitems > form:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(4) > a:nth-child(1)',
'1': '#mnuitems > form:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(4) > a:nth-child(1)',
'1.5': '#mnuitems > form:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(7) > td:nth-child(4) > a:nth-child(1)',
'2': '#mnuitems > form:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(10) > td:nth-child(4) > a:nth-child(1)',
'4': '#mnuitems > form:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(13) > td:nth-child(4) > a:nth-child(1)',
'6': '#mnuitems > form:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(16) > td:nth-child(4) > a:nth-child(1)',
}

bone_matrix{
'7': '#mnuitems > form:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(5) > td:nth-child(4) > a:nth-child(1)',
'10': '#mnuitems > form:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(8) > td:nth-child(4) > a:nth-child(1)',
'15': '#mnuitems > form:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(11) > td:nth-child(4) > a:nth-child(1)',
'25': '#mnuitems > form:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(14) > td:nth-child(4) > a:nth-child(1)',
'60': '#mnuitems > form:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(17) > td:nth-child(4) > a:nth-child(1)',
'120': '#mnuitems > form:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(20) > td:nth-child(4) > a:nth-child(1)',

}
