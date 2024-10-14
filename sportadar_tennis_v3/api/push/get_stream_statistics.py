from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.enum_push_event_type import EnumPushEventType
from ...models.get_stream_statistics_format import GetStreamStatisticsFormat
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    format_: Union[Unset, GetStreamStatisticsFormat] = UNSET,
    event_id: Union[Unset, List[EnumPushEventType]] = UNSET,
    competition_id: Union[Unset, List[str]] = UNSET,
    season_id: Union[Unset, List[str]] = UNSET,
    sport_id: Union[Unset, List[str]] = UNSET,
    sport_event_id: Union[Unset, List[str]] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_format_: Union[Unset, str] = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_.value

    params["format"] = json_format_

    json_event_id: Union[Unset, List[str]] = UNSET
    if not isinstance(event_id, Unset):
        json_event_id = []
        for event_id_item_data in event_id:
            event_id_item = event_id_item_data.value
            json_event_id.append(event_id_item)

    params["event_id"] = json_event_id

    json_competition_id: Union[Unset, List[str]] = UNSET
    if not isinstance(competition_id, Unset):
        json_competition_id = competition_id

    params["competition_id"] = json_competition_id

    json_season_id: Union[Unset, List[str]] = UNSET
    if not isinstance(season_id, Unset):
        json_season_id = season_id

    params["season_id"] = json_season_id

    json_sport_id: Union[Unset, List[str]] = UNSET
    if not isinstance(sport_id, Unset):
        json_sport_id = sport_id

    params["sport_id"] = json_sport_id

    json_sport_event_id: Union[Unset, List[str]] = UNSET
    if not isinstance(sport_event_id, Unset):
        json_sport_event_id = sport_event_id

    params["sport_event_id"] = json_sport_event_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/stream/statistics/subscribe",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.OK:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, GetStreamStatisticsFormat] = UNSET,
    event_id: Union[Unset, List[EnumPushEventType]] = UNSET,
    competition_id: Union[Unset, List[str]] = UNSET,
    season_id: Union[Unset, List[str]] = UNSET,
    sport_id: Union[Unset, List[str]] = UNSET,
    sport_event_id: Union[Unset, List[str]] = UNSET,
) -> Response[Any]:
    """Returns detailed, real-time information on every game statistics

    Args:
        format_ (Union[Unset, GetStreamStatisticsFormat]):
        event_id (Union[Unset, List[EnumPushEventType]]):
        competition_id (Union[Unset, List[str]]):
        season_id (Union[Unset, List[str]]):
        sport_id (Union[Unset, List[str]]):
        sport_event_id (Union[Unset, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        format_=format_,
        event_id=event_id,
        competition_id=competition_id,
        season_id=season_id,
        sport_id=sport_id,
        sport_event_id=sport_event_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    format_: Union[Unset, GetStreamStatisticsFormat] = UNSET,
    event_id: Union[Unset, List[EnumPushEventType]] = UNSET,
    competition_id: Union[Unset, List[str]] = UNSET,
    season_id: Union[Unset, List[str]] = UNSET,
    sport_id: Union[Unset, List[str]] = UNSET,
    sport_event_id: Union[Unset, List[str]] = UNSET,
) -> Response[Any]:
    """Returns detailed, real-time information on every game statistics

    Args:
        format_ (Union[Unset, GetStreamStatisticsFormat]):
        event_id (Union[Unset, List[EnumPushEventType]]):
        competition_id (Union[Unset, List[str]]):
        season_id (Union[Unset, List[str]]):
        sport_id (Union[Unset, List[str]]):
        sport_event_id (Union[Unset, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        format_=format_,
        event_id=event_id,
        competition_id=competition_id,
        season_id=season_id,
        sport_id=sport_id,
        sport_event_id=sport_event_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
