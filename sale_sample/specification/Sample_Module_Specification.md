## Module Name
sale_sample

### Requirement
* The module should allow the sales user to complete the sales process, and the price of sample product line does not include in the sales 

### Definitions
* Sample: Product sold as sample. 
* Object Definition: defnination

### Assumptions
* The price of the sample product is zero

### Implementation 

#### Sale Order line
##### Fields
*	Sale Order Line:
	** sample: boolean, the product is sample

##### Views
*	Sale Order Line
	**	Form View
	**	Tree View
	**	Kanban View


##### Report
*	Sale Order

##### Process
*	Sale Order
	** 	Here it describes how to implementate a function.
		set discount, final price and sub Total to zero when set sample is Ture.
		Line View in Sale Order
		Sample, Description, Quantity, UoM, Original Price, Discount, Final Price, Sub Total
	** 	Workflow
	** 	Function Processs

*sale order line
    **function: product_id_change_new  when onchange product, if is a sample SOL, price == 0
    **function: onchange_product_sample,if is a sample SOL, price == 0


##### Access Rights
* Sale Order
	**	Sale Manger can edit all
	**	Sales Own lead can op

