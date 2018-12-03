describe('My First Test', function() {
    it('Visit Student Page', function() {
        cy.visit('http://localhost:8080/')
    })

    it('Quering for Tableheaders', function(){
        cy.visit('http://localhost:8080/')
        cy.contains('ID')
        cy.contains('username')
        cy.contains('email')
    })

    it('Checking if Buttons clickable', function(){
        cy.visit('http://localhost:8080/')
        cy.contains('Delete Users').click()
        cy.contains('Add a new User').click()
        cy.contains('Get Data').click()
    })
})