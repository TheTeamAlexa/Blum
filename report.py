import aiofiles
import asyncio
from models import get_all

async def main():
    start_html = """
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Blum Report</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdn.datatables.net/1.11.5/css/dataTables.bootstrap5.min.css" rel="stylesheet">
    <style>tfoot { font-weight: bold; }</style>
</head>
<body>
    <div class="container mt-5">
        <h1 class="text-center mb-4">Blum Report</h1>
        <div class="table-responsive">
            <table id="dataTable" class="table table-striped table-hover">
                <thead class="table-dark">
                    <tr>
                        <th>ID</th>
                        <th>First Name</th>
                        <th>Balance</th>
                    </tr>
                </thead>
                <tbody>
"""
    end_html = lambda total: f"""
                </tbody>
                <tfoot class="table-light">
                    <tr>
                        <td colspan="2" class="text-end">Total Balance:</td>
                        <td class="text-end" id="totalBalance">{total}</td>
                    </tr>
                </tfoot>
            </table>
        </div>
    </div>

    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"></script>
    <script src="https://cdn.datatables.net/1.11.5/js/jquery.dataTables.min.js"></script>
    <script src="https://cdn.datatables.net/1.11.5/js/dataTables.bootstrap5.min.js"></script>

    <script>
        $(document).ready(function () {
            $('#dataTable').DataTable({
                "pageLength": 10,
                "lengthMenu": [[10, 25, 50, -1], [10, 25, 50, "All"]],
                "language": {
                    "lengthMenu": "Show _MENU_ entries per page",
                    "zeroRecords": "No matching data found",
                    "info": "Showing page _PAGE_ of _PAGES_",
                    "infoEmpty": "No data available",
                    "infoFiltered": "(filtered from _MAX_ total entries)",
                    "search": "Search:",
                    "paginate": {
                        "first": "First",
                        "last": "Last",
                        "next": "Next",
                        "previous": "Previous"
                    }
                }
            });
        });
    </script>
</body>
</html>
"""

    total_balance = 0
    rows = ""
    for record in await get_all():
        balance = float(record.get("balance", 0))
        total_balance += balance
        rows += f"""
<tr>
    <td>{record['id']}</td>
    <td>{record['first_name']}</td>
    <td>{balance}</td>
</tr>"""

    async with aiofiles.open("report.html", "w", encoding="utf-8") as file:
        await file.write(start_html + rows + end_html(total_balance))

    print(f"Total accounts: {len(await get_all())}")
    print(f"Total balance: {int(total_balance)}")
    print("HTML report generated at 'report.html'")

asyncio.run(main())
