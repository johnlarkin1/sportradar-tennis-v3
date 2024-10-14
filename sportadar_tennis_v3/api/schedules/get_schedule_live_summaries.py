from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_schedule_live_summaries_locale import GetScheduleLiveSummariesLocale
from ...types import Response


def _get_kwargs(
    locale: GetScheduleLiveSummariesLocale,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/{locale}/schedules/live/summaries",
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
    locale: GetScheduleLiveSummariesLocale,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    """get a list of summaries for live sport events

     Get a list of summaries for sport events which are live right now. Sport events appear in the feed
    10 minutes before the scheduled start time and are removed 10 minutes after the sport event is
    ended.

    Args:
        locale (GetScheduleLiveSummariesLocale):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        locale=locale,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    locale: GetScheduleLiveSummariesLocale,
    *,
    client: AuthenticatedClient,
) -> Response[Any]:
    """get a list of summaries for live sport events

     Get a list of summaries for sport events which are live right now. Sport events appear in the feed
    10 minutes before the scheduled start time and are removed 10 minutes after the sport event is
    ended.

    Args:
        locale (GetScheduleLiveSummariesLocale):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        locale=locale,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
