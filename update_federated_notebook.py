import nbformat as nbf


NOTEBOOK_PATH = "federated_learning.ipynb"

nb = nbf.read(NOTEBOOK_PATH, as_version=4)
part6_index = next(
    idx for idx, cell in enumerate(nb.cells)
    if cell.cell_type == "markdown" and "Part 6" in cell.source
)

nb.cells[part6_index + 1].source = """history = []


def weighted_average(metrics):
    total_examples = sum(num_examples for num_examples, _ in metrics)
    return {
        key: sum(num_examples * metric_values[key] for num_examples, metric_values in metrics) / total_examples
        for key in metrics[0][1]
    }


def average_parameters(client_results):
    total_examples = sum(num_examples for _, num_examples in client_results)
    averaged_parameters = []

    for parameter_group in zip(*(parameters for parameters, _ in client_results)):
        averaged_parameters.append(
            sum(parameter * num_examples for parameter, (_, num_examples) in zip(parameter_group, client_results))
            / total_examples
        )

    return averaged_parameters


def fit_config(server_round):
    return {\"local_epochs\": LOCAL_EPOCHS}


def server_evaluate(server_round, parameters, config):
    set_model_parameters(global_model, parameters)
    metrics = evaluate_global_model(global_model, client_loaders)
    loss = 1.0 - metrics[\"accuracy\"]

    if server_round > 0:
        history.append(
            {
                \"round\": server_round,
                \"loss\": loss,
                \"accuracy\": metrics[\"accuracy\"],
                \"precision\": metrics[\"precision\"],
                \"recall\": metrics[\"recall\"],
                \"f1\": metrics[\"f1\"],
                \"roc_auc\": metrics[\"roc_auc\"],
            }
        )

    return loss, {
        \"accuracy\": float(metrics[\"accuracy\"]),
        \"precision\": float(metrics[\"precision\"]),
        \"recall\": float(metrics[\"recall\"]),
        \"f1\": float(metrics[\"f1\"]),
        \"roc_auc\": float(metrics[\"roc_auc\"]),
    }


initial_model_parameters = get_model_parameters(global_model)
initial_parameters = ndarrays_to_parameters(initial_model_parameters)

strategy = fl.server.strategy.FedAvg(
    fraction_fit=1.0,
    fraction_evaluate=1.0,
    min_fit_clients=NUM_CLIENTS,
    min_evaluate_clients=NUM_CLIENTS,
    min_available_clients=NUM_CLIENTS,
    initial_parameters=initial_parameters,
    on_fit_config_fn=fit_config,
    evaluate_fn=server_evaluate,
    fit_metrics_aggregation_fn=weighted_average,
    evaluate_metrics_aggregation_fn=weighted_average,
)"""

nbf.write(nb, NOTEBOOK_PATH)
