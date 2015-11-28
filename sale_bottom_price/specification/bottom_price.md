## Module Name
* sale_bottom_price 
### Requirement
* The module should allow the sales user to complete the sales process, check List 3.1.
* This module allow sale order line to sync the final
* This module allow user to compare the price wiht product bottom price 

### Definitions
* Final Price: the price after the discount
* Original Price: the price taken from the price list
* Minimum Price: the bottom price for product

### Assumptions
* Product do not have any pre setup tax.
* bottom price is less than sale price
* All price is tax included. (Check AR/AP specification)

### Implementation 

#### Sale Order line
##### Fields
*	Sale Order Line:
	** final_price: float, the final price from the pricelist
	** subtotal_withtax: float, subtotal with tax in 
*	Product:
	** minimum_price: float, the bottom price of product

##### Views
*	Sale Order Line
	**	Form View
		![Order with final Price](/path/to/img.jpg "Sale Order Form View")
	**	Tree View
	**	Kanban View
*	Product 
	**      Form view
		after the sales price

##### Report
*	Sale Order
	**	Sale Report with final Price
	  	None of the reports should show the taxes applied to the SO.
	  	Quotation/Sale Order without discount () : 
	  	Requirements
	  	None of the reports should show the taxes applied to the SO.
	  	Report should be bilingual, label in this report should have Chinese and English. Check reference.
	  	shows the Final Price (old price_unit in standard OpenERP) and the Subtotal, but no the Discount.
	  	Description, Quantity, UoM, Final Price, Sub total
	**	Sale Report without final Price
		Report descriptions


##### Process
*	Sale Order
	** 	Here it describes how to implementate a function.
		Update discount when updating final price, update final price when updating the discount price.
		Line View in Sale Order
		Description, Quantity, UoM, Original Price, Discount, Final Price, Sub Total
		if the Final Price is less than the bottom price, the system will pop a warning message
	** 	Workflow
	** 	Function Process

##### Access Rights
* Sale Order
	**	Sale Manger can edit all
	**	Sales Own lead can op

