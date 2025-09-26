from prefect import flow
from tasks.customer_tasks import get_customer_ids, process_customer


@flow
def main() -> list[str]:
    """Main flow that processes customer data."""
    customer_ids = get_customer_ids()
    # Map the process_customer task across all customer IDs
    results = process_customer.map(customer_ids)
    return results



if __name__ == "__main__":
    main()