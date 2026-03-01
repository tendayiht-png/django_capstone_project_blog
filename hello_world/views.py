from django.http import JsonResponse
from .models import GameScore
import json

def save_score(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        GameScore.objects.create(
            user=request.user,
            score=data.get('score'),
            incorrect=data.get('incorrect'),
            game_type=data.get('game_type')
        )
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)
