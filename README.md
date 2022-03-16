# fromZipToFolder

Automate E-Arşiv Invoice organizing process with Python
Since, I started reading Automate Boring Stuff with Python written by Al Sweigart, I am asking myself what boring stuff can I automatewith python in my daily life. 
Answer was organazing() my company invoices accordingto their dates. 
By the Turkish trade law person or company can use https://earsivportal.efatura.gov.tr for creating invoices. 
If invoice amount exceeds 7000TL person/company should issue the invoice via this system. 
Also invoices needs to be kept for 10 years by law, so keeping organized invoices is very important.
There can be thousands of invoices within a year or by month depending on person/company, so it can get very messy and time consuming to organize the invoices manually. 
In my opinion, best way to keep these invoices are is keep them in year.month folders and renaming the files by first and second word of customers name.
When invoice issued in https://earsivportal.efatura.gov.tr issuer can download it as a zip file containing 2 files with a .html(actual invoice) and .xml extension.

Without code, process will look like this:
* open source directory >>
* open zip file >>
* open invoice(to see customer name) >>
* open target desination >>
* check whether there is a year.month folder, if not create it >>
* extract the invoice to corresponding year.month folder at target directory >>
* rename the invoice file to customer_name-day.month format 

This function automizes this process. Detailed version of usage of this function will be explained in a medium post link will be posted <here>.
