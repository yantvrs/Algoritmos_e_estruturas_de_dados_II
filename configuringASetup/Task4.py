import itertools
from Setups import CarSetups
from Setups import bottles
from Setups import drivers

# Crie uma lista de todas as combinações possíveis de peças, pilotos e garrafas
setup_combinations = list(
    itertools.product(CarSetups.breaksOptions, CarSetups.gearBoxesOptions, CarSetups.rearWingsOptions,
                      CarSetups.frontWingsOptions, CarSetups.suspensionsOptions, CarSetups.enginesOptions,
                      drivers.keys(), bottles.keys()))

# Inicialize variáveis para rastrear a melhor configuração e sua pontuação
melhor_configuracao = None
melhor_pontuacao = 0

# Itere por todas as combinações e calcule a pontuação da equipe
for setup in setup_combinations:
    breaks, gearBox, rearWing, frontWing, suspension, engine, piloto, garrafa = setup
    car_setup = CarSetups(breaks, gearBox, rearWing, frontWing, suspension, engine)

    # Verifique se as métricas do piloto e da garrafa existem
    if piloto in drivers and garrafa in bottles:
        piloto_metrics = drivers[piloto]
        garrafa_metrics = bottles[garrafa]

        # Calcule a pontuação da equipe com base nas contribuições do carro, piloto e garrafa
        team_score = car_setup.sum_contributions()
        for metric, value in piloto_metrics.items():
            if metric in team_score:
                team_score[metric] += value
        for metric, value in garrafa_metrics.items():
            if metric in team_score:
                team_score[metric] += value

        # Calcule a pontuação da equipe com base na fórmula especificada
        if "averagePitStopTime" in team_score:
            team_score = team_score["speed"] + team_score["cornering"] + team_score["powerUnit"] + team_score[
                "reliability"] + (team_score["averagePitStopTime"] / 0.02)

        if team_score > melhor_pontuacao:
            melhor_pontuacao = team_score
            melhor_configuracao = setup

# Imprima a melhor configuração e sua pontuação
print("Melhor Configuração:")
print("Piloto:", melhor_configuracao[6])
print("Garrafa:", melhor_configuracao[7])
print("Pontuação da Equipe:", melhor_pontuacao)