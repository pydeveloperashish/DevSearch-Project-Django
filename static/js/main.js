// Get SearchForm and Page Links
let searchForm = document.getElementById('searchForm');
let pageLinks = document.getElementsByClassName('page-link');
// Ensure SearchForm Exists
if (searchForm) {
    for (let i = 0; pageLinks.length > i; i++) {
        pageLinks[i].addEventListener('click', function (e) {
            e.preventDefault();
            // Get The Data Attribute
            let page = this.dataset.page;
            // console.log(page); 

            // Add Hidden Search Input to Form
            searchForm.innerHTML += `<input value=${page} name="page" 
                hidden/>`
            // Submit Form
            searchForm.submit();
        })
    }
}
