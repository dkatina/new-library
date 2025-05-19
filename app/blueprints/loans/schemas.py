from app.extensions import ma
from app.models import Loan

class LoanSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Loan
        include_fk = True

loan_schema = LoanSchema()
loans_schema = LoanSchema(many=True)