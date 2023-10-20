from configuringASetup.Setups import bottles
from configuringASetup.Setups import drivers
from configuringASetup.Setups import CarSetups

all_setups = []
team_scores = []
cutoff = 880
setup_id = 'Setup '
id_count = 0
for breaks in CarSetups.breaksOptions:
    for gearBox in CarSetups.gearBoxesOptions:
        for rearWing in CarSetups.rearWingsOptions:
            for frontWing in CarSetups.frontWingsOptions:
                for suspension in CarSetups.suspensionsOptions:
                    for engine in CarSetups.enginesOptions:
                        setup = CarSetups(breaks, gearBox, rearWing, frontWing, suspension, engine)
                        contributions = setup.sum_contributions()

                        setup_data = {
                            "id": setup_id + str(id_count),
                            "setup": setup,
                            "contributions": contributions
                        }
                        all_setups.append(setup_data)

# Crie uma lista de todas as combinações possíveis de peças, pilotos e garrafas
setup_combinations = all_setups

# Inicialize variáveis para rastrear a melhor configuração e sua pontuação
melhor_configuracao = None
melhor_pontuacao = 0

# Itere por todas as combinações e calcule a pontuação da equipe
for setup in setup_combinations:
    breaks, gearBox, rearWing, frontWing, suspension, engine, piloto, garrafa = setup
    car_setup = CarSetups(breaks, gearBox, rearWing, frontWing, suspension, engine)
    piloto_metrics = drivers[piloto]
    garrafa_metrics = bottles[garrafa]

    # Calcule a pontuação da equipe com base nas contribuições do carro, piloto e garrafa
    team_score = car_setup.sum_contributions()
    for metric, value in piloto_metrics.items():
        team_score[metric] += value
    for metric, value in garrafa_metrics.items():
        team_score[metric] += value

    # Calcule a pontuação da equipe com base na fórmula especificada no Slide 18
    # (soma das métricas dos 2 motoristas + velocidade + curvas + unidade de potência + confiabilidade + (média de parada nos boxes) / 0,02)
    team_score = team_score["overtaking"] + team_score["defending"] + team_score["qualifying"] + team_score["race_start"] + team_score["tyre_management"] + team_score["speed"] + team_score["cornering"] + team_score["powerUnit"] + team_score["reliability"] + (team_score["averagePitStopTime"] / 0.02)

    if team_score > melhor_pontuacao:
        melhor_pontuacao = team_score
        melhor_configuracao = setup

# Imprima a melhor configuração e sua pontuação
print("Melhor Configuração:")
print("Piloto:", melhor_configuracao[6])
print("Garrafa:", melhor_configuracao[7])
print("Pontuação da Equipe:", melhor_pontuacao)